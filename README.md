**!! CONVERSION TYPES !!**

**IMAGES**
~~png - ico~~
~~ico - png/jpeg~~

~~png - jpeg~~
~~jpeg - png~~

~~avif - jpg~~
~~avif - png~~

**PDF**
~~pdf - png/jpeg~~
~~jpeg/png - pdf~~

word to pdf
pdf to word

pdf compression


**MISC**
svg - png/jpeg - TBA
png/jpeg - svg - TBA

--------------------------



* pip install -r requirements.txt

NOTE: If converting to .ico - first convert .jpg (or whatever format you have) to .png as .jpg doesn't support transparency which is often needed for .ico --- only convert png to ico feature has been added


- while converting, add better suffix - e.g. "converted_ico" to show the format even if extension is hidden

- output message in is the terminal for now - later it should be added to converter app

- poppler binaries are included into poppler/bin for the pdf - img conversions

- when converting img to pdf user can choose to convert one image per pdf or to bundle them into one pdf


**TO DO**

In case of larger PDFs, user should be able to choose which page he wants to convert to either img or docx

like Image to PDF conversion, where user can choose to create multiple or single PDF in case of multiple images, image to image conversions could be bundled up - convert to JPG/PNG/ICO can be located in the same button and user can get a pop-up to choose file type he needs

in Image to PDF, fix X button to do the same thing as Cancel button

Batch conversion enabled wherever possible

Remove convert_files if not necessary, leave only convert_files

When doing PDF compression, add slider to allow user to sacrifice quality for smaller PDF size

Allow saving all files to one folder automatically - default download directory? maybe either root folder or rather /Downloads (or ask user to decide)

For now all converted files are getting saved in the location of original files. User can be asked to choose download directory.
Additionally, instead of printing a message in terminal, add successful conversion message after conversion is done (delete all the terminal message from the code later)

Keep Info button updated