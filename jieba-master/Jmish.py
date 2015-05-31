#!/usr/bin/python
# -*- coding: utf-8 -*-
print("Content-type: text/html")
print ""



print  "----------------------------------------------"
f = open("/home/mish/Web/B.txt", "w+")  
f.write( "TestMishCC")
f.close()

#print  "----------------------------------------------"

import jieba
import cgi
import webbrowser

#def contact():
    #webbrowser.open('http://umkkaea539e4.mish.koding.io/eyeinfo/eyeinfo.html', new=1, autoraise=False)
form = cgi.FieldStorage()
textG = form['text'].value
#textG = "Fuck u!!"
print  "----------------~------------------------------"
if textG is None:
  textG = "NONE..."
#print"明天他演講到一半站起來幫她唱生日快樂歌"
#print textG
seg_list = jieba.cut(textG.decode('utf-8'), cut_all=False)
#print seg_list
a = "/ ".join(seg_list).encode('utf-8')

print a
#print "Content-Type:application/octet-stream; name=\"FileName\"\r\n";
#content = urllib2.urlopen('http://umkkaea539e4.mish.koding.io/eyeinfo/eyeinfo.html')
#print content

print "<h2> Entered Text Content is %s </h2>" % a
    
    #return render_to_response('eyeinfo.html', {'form': form,})
#return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
#print('http://umkkaea539e4.mish.koding.io/eyeinfo/eyeinfo.html')

#return render_to_response('Home.html')

#webbrowser.open('../eyeinfo/eyeinfo.html', new=1, autoraise=False)

#GenericBrowser('links').open_new('http://umkkaea539e4.mish.koding.io/eyeinfo/eyeinfo.html')
#google = raw_input('Google search:')
#webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % google)


#print  "~~~----------------------------------------------"
#contact_form = ContactForm(request.POST)
#ctx = {'contact_form':contact_form}
#return render_to_response('Web/eyeinfo/eyeinfo.html', ctx , context_instance=RequestContext(request))




#print  "----------------------------------------------"
