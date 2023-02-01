from aip import AipOcr # full name is baidu-aip which is used for baiduAI interfaces.    We can type 'CTRL' and click AipOcr to check the funtion that we need.

#identity authentication (APPID APIKEY SECRETKEY)
APP_ID='26236017'
API_KEY='gujx0zRm9ICE0ddHbWPdjYCo'
SECRET_KEY='tHDVQlbwyl5YKatVaHo0mifd0hWSxLEc'

client = AipOcr(APP_ID,API_KEY,SECRET_KEY)

# get image
def get_file_content(file):
    with open(file,'rb') as f: # open the file we need   'rb' r means 'read' and 'b' means 'binary data'
        return f.read() #The rusult is binary strings

# extract texts
def img_to_str(image_path):
    image = get_file_content(image_path)
    print(image)       #if we print image, the result is binary strings
    result = client.basicGeneral(image) #we use the funtion basicGeneral of AipOcr to translate the binary strings to texts that we can understand
    # in the prevous step, we used BaiduAI character recognition interface for data processing. We converted
    # the binary strings into words that we can understand.
    print(result)


img_to_str('demo.png')