push:
	git push --all git@github.com:oubiwann/innoth.git
	git push --all ssh://oubiwann@emotionalmodels.git.sourceforge.net/gitroot/emotionalmodels/emotionalmodels

clean-repo:
	rm -rf .git/refs/original/
	git reflog expire --expire=now --all
	git gc --aggressive --prune=now
