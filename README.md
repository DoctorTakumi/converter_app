Add support for multiple files at once - batch conversion - DONE for images
Allow saving all files to one folder automatically - default download directory? maybe either root folder or rather /Downloads (or ask user to decide)
Quality slider - adjust compression/quality settings - how? if...quality slider


What conversion types do I want?
Separate conversions from compressions? Possible? Plausible?


-----------------------

**!! CONVERSION TYPES !!**

**IMAGES**
~~png/jpeg - ico~~ - DONE (only png - jpeg isn't suitable for that)
~~ico - png/jpeg~~ - DONE

~~png - jpeg~~ - DONE
~~jpeg - png~~ - DONE

**PDF**
pdf - png/jpeg
jpeg/png - pdf

pdf shrink
word to pdf
pdf to word

- add .avif to jpg/png

**MISC**
~~svg - png/jpeg~~ - irrelevant for now
~~png/jpeg - svg~~ - irrelevant for now

--------------------------




* pip install -r requirements.txt

NOTE: If converting to .ico - first convert .jpg (or whatever format you have) to .png as .jpg doesn't support transparency which is often needed for .ico --- only convert png to ico


- while converting, add better suffix - e.g. "converted_ico" to show the format even if extension is hidden