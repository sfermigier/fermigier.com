.PHONY:
develop:
	yarn run develop

.PHONY:
format:
	yarn run prettier --write --trailing-comma es5 \
		*.js src/**/*.vue src/*/**.js

.PHONY:
build:
	npm run build
	rsync -a assets/* dist/assets
	rsync -a assets/images dist/
	rsync -a assets/videos dist/static/

.PHONY:
push:
	rsync -e ssh -avz --delete-after \
		dist/ web@bulma:/var/www/fermigier.com/

.PHONY:
deploy: build push

.PHONY:
clean:
	rm -rf dist src/.temp


run:
	watchmedo shell-command \
		--patterns="*.py;*.j2" \
		--recursive \
		--command='alamo build' \
		.
