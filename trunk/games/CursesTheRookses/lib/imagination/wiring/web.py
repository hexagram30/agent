
# web

from twisted.internet import defer
from twisted.python import log

from imagination import iimagination
from imagination.text import english
from imagination import errors

from nevow import inevow
from nevow import rend
from nevow.loaders import stan
from nevow.tags import *
from nevow.liveevil import handler, glue, literal
from nevow import entities

getinput = literal.getinput
getNode = literal.document.getElementById


class WebPage(rend.Page):
    def render_handler(self, ctx, data):
        actorTemplate = self.original
        def handle_login(client, username):
            self.client = client
            self.avatar = actorTemplate[
                    iimagination.IUI: lambda x: self
                ].fill(
                    english.INoun, name=username).new()

            self.inputline = [
                div[username],
                form(onsubmit=handler(self.handle_userinput, getinput()))[
                    input(id="user-input"), input(type="submit", value="do")]]

            client.set('inputline', self.inputline)
            client.set('output',
                h1["Welcome to your doom"])
            self.handle_userinput(client, 'look')
        return handler(handle_login, getNode('username').value)

    ## This is the splashpage which asks for login information. It will be replaced, after login
    ## with the interactive ui.
    docFactory = stan(html[
        head[
            glue,
            script(type="text/javascript")[
                """function getinput() { return document.getElementById('user-input').value } """],
            style(type='text/css')[
                """
#inputline { border: 1px solid black;
background-color: #efefef;
padding: 0.5em;
margin-top: 0.5em; }

.clickable { cursor: pointer; color: blue; text-decoration: underline; }
"""]],
        body[
            div(id="output"), ## Scrollback goes here
            div(id="inputline")[ ## after login the inputline goes here
            h1["How are you gentlemen"],
            p["For great justice username"],
            form(onsubmit=render_handler)[
                input(type="text", id="username"), input(type="submit", value="login")]]],
            div(id="bottommost")[entities.nbsp]]) ## scrollIntoView this, to ensure we stay at the bottom of the page

    def write(self, what):
        self.client.append('output', what)

    def clearInput(self):
        self.client.sendScript("var ui = document.getElementById('user-input'); ui.value = ''; document.getElementById('bottommost').scrollIntoView(); ui.focus();")

    def handle_userinput(self, client, cmd):
        if not cmd.strip(): return
        self.write(div['>', cmd])
        self.clearInput()
        d = defer.maybeDeferred(english.IThinker(self.avatar).parse, cmd)
        d.addErrback(self._ebParsed)

    def _ebParsed(self, failure):
        if failure.check(errors.RealityException):
            self.write(english.express(failure.value, self.avatar))
        else:
            self.write("Internal parse error: %s\r\n" % (failure.value,))
            log.err(failure)

    def presentMenu(self, list, typename=None):
        """Present 'list' of 'typename's as a menu to the user; return a
        Deferred of an index into the list.
        """
        d = defer.Deferred()
        def handle_choice(client, index):
            try:
                index = int(index)
            except:
                return
            if index < 0 or index >= len(list): return
            client.set('inputline', self.inputline)
            self.client.sendScript("document.onkeypress = '';");
            self.clearInput()
            d.callback(index)
        self.client.sendScript(
            self.client.flt([literal("document.onkeypress = function(event) { "),
            handler(handle_choice, literal('parseInt(String.fromCharCode(event.which))-1')),
            literal("}")], quote=False))
        self.client.set('inputline',
            [
                strong["Which ", typename or "thing", " do you mean?"],
                ol[
                [li(_class='clickable', onclick=handler(handle_choice, str(index)))[
                    english.express(val, self.avatar)]
                for (index, val) in enumerate(list)]]])

        return d

    def presentEvent(self, iface, event):
        """Present an event!
        """
        ## Hack to elide ANSI for now.
        if isinstance(event, str) and event.startswith(chr(27)):
            event = strong[english.express(event[5:-4], self.avatar)]
        else:
            event = english.express(event, self.avatar)
        self.write(div[event])
