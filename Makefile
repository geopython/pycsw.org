BUILDDIR=_site

html:
	jekyll build

drafts:
	jekyll build --drafts

linkcheck:
	check-links $(BUILDDIR)

clean:
	rm -fr $(BUILDDIR)/*

publish: html
	find $(BUILDDIR) -type f -exec chmod 664 {} \;
	find $(BUILDDIR) -type d -exec chmod 775 {} \;
	./publish.sh $(username)
