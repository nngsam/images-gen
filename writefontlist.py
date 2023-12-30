import os 

#writing font list 
#list_fonts = os.listdir(os.path.join(os.getcwd(), 'font'))
#list_fonts.sort()
#print(list_fonts[1])

#with open(os.path.join(os.getcwd(), 'font_list/font_list.txt'), 'w') as f: 
    #for item in list_fonts: 
        #f.write(item) 
        #f.write('\n')
        

# For changing file names 

'''directory = os.path.join(os.getcwd(), 'font')
files = os.listdir(directory)
files.sort()
count = 1 
for filename in files: 
    if os.path.isfile(os.path.join(directory,filename)): 
        newname = f'font{count}.ttf'
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, newname)
        os.rename(old_path,new_path)
        count += 1 
print('Completed renaiming')'''

#Count number of images
parent = 'effect_layout_image'
count_img = 0 
for folder in os.listdir(parent): 
    effect_folder = os.path.join(parent,folder)
    count_img += len(os.listdir(os.path.join(effect_folder,'images')))
print(count_img)

#Count: 828k images
#print(os.listdir(parent))



