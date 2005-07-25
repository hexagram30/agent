#!/usr/bin/python2
#
# Urwid html fragment output wrapper for "screen shots"
#    Copyright (C) 2004-2005  Ian Ward
#
#    This library is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Lesser General Public
#    License as published by the Free Software Foundation; either
#    version 2.1 of the License, or (at your option) any later version.
#
#    This library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with this library; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# Urwid web site: http://excess.org/urwid/

"""
HTML PRE-based UI implementation
"""

import util

try: True # old python?
except: False, True = 0, 1
                

_html_colours = {
	'black':		"black",
	'dark red':		"#c00000",
	'dark green':		"green",
	'brown':		"#804000",
	'dark blue':		"#0000c0",
	'dark magenta':		"#c000c0",
	'dark cyan':		"teal",
	'light gray':		"silver",
	'dark gray':		"gray",
	'light red':		"#ff6060",
	'light green':		"lime",
	'yellow':		"yellow",
	'light blue':		"#8080ff",
	'light magenta':	"#ff40ff",
	'light cyan':		"aqua",
	'white':		"white",
}

# replace control characters with ?'s
_trans_table = "?" * 32 + "".join([chr(x) for x in range(32, 256)])

class HtmlGeneratorSimulationError(Exception):
	pass

class HtmlGenerator:
	# class variables
	fragments = []
	sizes = []
	keys = []

	def __init__(self):
		self.palette = {}
		self.has_color = True
	
	def register_palette( self, l ):
		"""Register a list of palette entries.

		l -- list of (name, foreground, background) or
		     (name, same_as_other_name) palette entries.

		calls self.register_palette_entry for each item in l
		"""
		
		for item in l:
			if len(item) in (3,4):
				self.register_palette_entry( *item )
				continue
			assert len(item) == 2, "Invalid register_palette usage"
			name, like_name = item
			if not self.palette.has_key(like_name):
				raise Exception("palette entry '%s' doesn't exist"%like_name)
			self.palette[name] = self.palette[like_name]

	def register_palette_entry( self, name, foreground, background, 
		mono=None):
		"""Register a single palette entry.

		name -- new entry/attribute name
		foreground -- foreground colour
		background -- background colour
		mono -- monochrome terminal attribute

		See curses_display.register_palette_entry for more info.
		"""
		if foreground == "default":
			foreground = "black"
		if background == "default":
			background = "light gray"
		self.palette[name] = (foreground, background, mono)

	def run_wrapper(self,fn):
		"""Call fn."""
		return fn()

	def draw_screen(self, (cols, rows), r ):
		"""Create an html fragment from the render object. 
		Append it to HtmlGenerator.fragments list.
		"""
		# collect output in l
		l = []
		
		lines = r.text
		
		assert len(lines) == rows
	
		if r.cursor is not None:
			cx, cy = r.cursor
		else:
			cx = cy = None
		
		for y in range(len(lines)):
			line = lines[y].translate( _trans_table )
				
			if len(r.attr) > y:
				attr = r.attr[y]
			else:
				attr = []
			col = 0
			
			for a, run in attr:
				if a is None:
					fg,bg,mono = "black", "light gray", None
				else:
					fg,bg,mono = self.palette[a]
				if y == cy:
					l.append( html_span( line[col:col+run],
						fg, bg, cx-col ))
				else:
					l.append( html_span( line[col:col+run],
						fg, bg ))
				col += run

			if cols > col:
				fg,bg,mono = "black", "light gray", None
				end = line[col:]+" "*(cols-len(line))
				if y == cy:
					l.append( html_span( end, 
						fg, bg, cx-col ))
				else:
					l.append( html_span( end,
						fg, bg ))
			l.append("\n")
						
		# add the fragment to the list
		self.fragments.append( "<pre>%s</pre>" % "".join(l) )
			
			
	def get_cols_rows(self):
		"""Return the next screen size in HtmlGenerator.sizes."""
		if not self.sizes:
			raise HtmlGeneratorSimulationError, "Ran out of screen sizes to return!"
		return self.sizes.pop(0)

	def get_input(self):
		"""Return the next list of keypresses in HtmlGenerator.keys."""
		if not self.keys:
			raise HtmlGeneratorSimulationError, "Ran out of key lists to return!"
		return self.keys.pop(0)
	

def html_span( s, fg, bg, cursor = -1):
	html_fg = _html_colours[ fg ]
	html_bg = _html_colours[ bg ]
	
	if cursor >= 0 and cursor < len(s):
		# use an underline to approximate a cursor
		c2 = cursor +1
		w = util.within_double_byte(s, 0, cursor)
		if w == 1:
			c2 += 1
		if w == 2:
			cursor -= 1
		escaped = html_escape(s[:cursor]) + "<u>" + html_escape(s[cursor:c2]) + "</u>" + html_escape(s[c2:])
	else:
		escaped = html_escape(s)
	
	return '<span style="color:%s;background:%s">%s</span>' % (html_fg, html_bg, escaped)


def html_escape(text):
	"""Escape text so that it will be displayed safely within HTML"""
	text = text.replace('&','&amp;')
	text = text.replace('<','&lt;')
	text = text.replace('>','&gt;')
	return text

def screenshot_init( sizes, keys ):
	"""Replace curses_display.Screen class with HtmlGenerator.
	
	Call this function before executing an application that uses 
	curses_display.Screen to have that code use HtmlGenerator instead.
	
	sizes -- list of ( columns, rows ) tuples to be returned by each call
	         to HtmlGenerator.get_cols_rows()
	keys -- list of lists of keys to be returned by each call to
	        HtmlGenerator.get_input()
	
	Lists of keys may include "window resize" to force the application to
	call get_cols_rows and read a new screen size.

	For example, the following call will prepare an application to:
	 1. start in 80x25 with its first call to get_cols_rows()
	 2. take a screenshot when it calls draw_screen(..)
	 3. simulate 5 "down" keys from get_input()
	 4. take a screenshot when it calls draw_screen(..)
	 5. simulate keys "a", "b", "c" and a "window resize"
	 6. resize to 20x10 on its second call to get_cols_rows()
	 7. take a screenshot when it calls draw_screen(..)
	 8. simulate a "Q" keypress to quit the application

	screenshot_init( [ (80,25), (20,10) ],
		[ ["down"]*5, ["a","b","c","window resize"], ["Q"] ] )
	"""
	try:
		for (row,col) in sizes:
			assert type(row) == type(0)
			assert row>0 and col>0
	except:
		raise Exception, "sizes must be in the form [ (col1,row1), (col2,row2), ...]"
	
	try:
		for l in keys:
			assert type(l) == type([])
			for k in l:
				assert type(k) == type("")
	except:
		raise Exception, "keys must be in the form [ [keyA1, keyA2, ..], [keyB1, ..], ...]"
	
	import curses_display
	curses_display.Screen = HtmlGenerator
	
	HtmlGenerator.sizes = sizes
	HtmlGenerator.keys = keys


def screenshot_collect():
	"""Return screenshots as a list of HTML fragments."""
	l = HtmlGenerator.fragments
	HtmlGenerator.fragments = []
	return l

	
