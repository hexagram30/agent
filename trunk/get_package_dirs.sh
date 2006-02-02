find . -type d| \
egrep -v 'svn|build|sandbox|third-party'| \
sed "s/\.\//'/g"| \
sed "s/$/',/g"| \
egrep -v "\.',"
