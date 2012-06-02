REMOVE_PATTERN ?= DO-NOT-RUN-WITHOUT-SETTING-THIS

push:
	git push --all git@github.com:oubiwann/innoth.git
	git push --all ssh://oubiwann@emotionalmodels.git.sourceforge.net/gitroot/emotionalmodels/emotionalmodels

clean-repo:
	rm -rf .git/refs/original/
	git reflog expire --expire=now --all
	git gc --aggressive --prune=now
	du -sh .git

remove-matching:
	git filter-branch --index-filter \
	'git rm -r --cached --ignore-unmatch $(REMOVE_PATTERN)'\
	--prune-empty -- --all

remove-and-clean: remove-matching clean-repo
