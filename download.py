import os,urllib2,urllib  

path='D:\DownLoad'    
file_name='collision.csv'   
dest_dir=os.path.join(path,file_name)  
  
url='https://data.cityofnewyork.us/api/views/h9ginx95/rows.csv?accessType=DOWNLOAD'
def downLoadPicFromURL(dest_dir,URL):  
        try:  
          urllib.urlretrieve(url , dest_dir)  
        except:  
          print '\tError retrieving the URL:', dest_dir  
downLoadPicFromURL(dest_dir,url)
