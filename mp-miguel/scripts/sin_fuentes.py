"""Copia de un .docx sin las fuentes incrustadas, para subirlo a Drive y convertirlo en Google Doc
(Docs usa sus propias fuentes: Montserrat, Lora... son de Google Fonts). No toca document.xml."""
import re, sys, zipfile
src, dst = sys.argv[1:3]
zin = zipfile.ZipFile(src)
zout = zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED, compresslevel=9)
for i in zin.infolist():
    if i.filename.startswith('word/fonts/'): continue
    data = zin.read(i.filename)
    if i.filename == 'word/fontTable.xml':
        data = re.sub(rb'<w:embed(Regular|Bold|Italic|BoldItalic)[^>]*/>', b'', data)
    if i.filename == 'word/_rels/fontTable.xml.rels':
        data = re.sub(rb'<Relationship [^>]*Target="fonts/[^"]*"[^>]*/>', b'', data)
    if i.filename == '[Content_Types].xml':
        data = re.sub(rb'<Default Extension="(ttf|odttf)"[^>]*/>', b'', data)
    zout.writestr(i, data)
zout.close()
