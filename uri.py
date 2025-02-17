from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.chrome.options import Options
import os
import time
from PIL import Image

options = Options();
options.binary_location = '/opt/google/chrome/google-chrome';
browser=webdriver.Chrome(executable_path='./chromedriver',chrome_options=options)
#browser.get("https://csacademy.com/contests/");
	
url = "https://www.urionlinejudge.com.br/judge/en/users/university/iitmand?page=";

i = 1;
import os
import time

from PIL import Image

def fullpage_screenshot(driver, file):

        print("Starting chrome full page screenshot workaround ...")

        total_width = driver.execute_script("return document.body.offsetWidth")
        total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
        viewport_width = driver.execute_script("return document.body.clientWidth")
        viewport_height = driver.execute_script("return window.innerHeight")
        print("Total: ({0}, {1}), Viewport: ({2},{3})".format(total_width, total_height,viewport_width,viewport_height))
        rectangles = []

        i = 0
        while i < total_height:
            ii = 0
            top_height = i + viewport_height

            if top_height > total_height:
                top_height = total_height

            while ii < total_width:
                top_width = ii + viewport_width

                if top_width > total_width:
                    top_width = total_width

                print("Appending rectangle ({0},{1},{2},{3})".format(ii, i, top_width, top_height))
                rectangles.append((ii, i, top_width,top_height))

                ii = ii + viewport_width

            i = i + viewport_height

        stitched_image = Image.new('RGB', (total_width, total_height))
        previous = None
        part = 0

        for rectangle in rectangles:
            if not previous is None:
                driver.execute_script("window.scrollTo({0}, {1})".format(rectangle[0], rectangle[1]))
                print("Scrolled To ({0},{1})".format(rectangle[0], rectangle[1]))
                time.sleep(0.2)

            file_name = "part_{0}.png".format(part)
            print("Capturing {0} ...".format(file_name))

            driver.get_screenshot_as_file(file_name)
            screenshot = Image.open(file_name)

            if rectangle[1] + viewport_height > total_height:
                offset = (rectangle[0], total_height - viewport_height)
            else:
                offset = (rectangle[0], rectangle[1])

            print("Adding to stitched image with offset ({0}, {1})".format(offset[0],offset[1]))
            stitched_image.paste(screenshot, offset)

            del screenshot
            os.remove(file_name)
            part = part + 1
            previous = rectangle

        stitched_image.save(file)
        print("Finishing chrome full page screenshot workaround...")
        return True
def down(driver,file):
	element = driver.find_element_by_tag_name('body');
	foot = driver.find_element_by_tag_name('footer');
	driver.execute_script("arguments[0].setAttribute('style','display:none;')",foot);
	element_png = element.screenshot_as_png
	with open(file,"wb") as f:
		f.write(element_png); 
while i<=10:
	s = str(i);
	print(s);
	i+=1;
	browser.get(url+s);
	print("uri/"+url+s+".png");
	#browser.get_screenshot_as_file("uri/"+s+".png");
	down(browser,"uri/"+s+".png");

browser.close();