#!/usr/bin/env python
# coding: utf-8

# In[1]:


#TODO 1: Lorem Ipsum is just a random txt that devs use as a placeholder for multiple things (especially
#web developping) when you don't have the real text and just want to test your functionnality. 
#Put a Lorem Ipsum of 3 paragraphs in a txt file using python, each paragraph delimited by two new line.


# In[2]:


import tqdm


# In[3]:


lorem_ipsum="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent fringilla molestie dolor et lobortis. Praesent sed lobortis elit, id cursus augue. Pellentesque mauris nulla, hendrerit eget erat dignissim, rutrum cursus nisi. Morbi sit amet posuere enim. Mauris iaculis sapien a tincidunt cursus. Praesent blandit nisi eget justo sagittis fermentum. In sed ligula vel nisl viverra faucibus a ac urna. Suspendisse nec hendrerit massa. Mauris sagittis ante commodo ante dignissim, et euismod ex porttitor. Vestibulum in turpis viverra, aliquet magna id, interdum libero.\nNulla accumsan maximus risus ut interdum. Nam suscipit ligula ac ante finibus fermentum. Fusce at euismod nibh. In dignissim nisl eget ligula pulvinar, vitae fermentum elit sodales. Donec condimentum, justo at consequat tincidunt, tortor ex facilisis nulla, vel aliquet purus metus vel mauris. Sed in erat rutrum, pulvinar ligula dignissim, convallis dolor. Fusce eget urna eleifend elit malesuada porttitor. Aenean elementum eu mi vitae pretium. Mauris odio est, sodales sit amet rutrum eu, egestas vitae dolor. Duis fermentum justo ipsum, tincidunt commodo mi dignissim eget. Aenean sit amet venenatis felis. Donec scelerisque aliquet maximus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam et rhoncus nulla. Nam vitae metus posuere ex congue blandit. Pellentesque vehicula elit leo.\nEtiam mattis diam eget aliquam condimentum. Fusce non egestas tellus, sed posuere lorem. Suspendisse purus felis, semper in convallis non, cursus id felis. Phasellus euismod, sem volutpat volutpat dictum, ex urna aliquam felis, fermentum porta enim nisi quis arcu. Proin lacinia urna eget urna eleifend, malesuada rhoncus tortor porttitor. Ut sed mi vitae odio ultricies tempor. Etiam bibendum ligula quis felis lobortis imperdiet. Praesent eleifend ex vitae quam molestie, at luctus libero efficitur. Donec pretium posuere ipsum. Pellentesque vulputate, leo a convallis accumsan, mauris risus convallis odio, vel viverra tellus neque sit amet nulla. Proin sit amet ante sit amet massa convallis vestibulum nec eget enim. Nulla eget sem neque. In finibus arcu in egestas vehicula."


# In[4]:


lorem_ipsum


# In[5]:


with open("lorem_ipsum.txt", "w") as file:
        file.write(lorem_ipsum+ "\n\n")
        file.write(lorem_ipsum+ "\n\n")
        file.write(lorem_ipsum)
    


# In[6]:


p = lorem_ipsum.split('\n')


# In[7]:


p


# In[8]:


p[1]


# In[9]:


with open("lorem_ipsum.txt", "w") as file:
    file.write(p[0] + "\n\n")
    file.write(p[1] + "\n\n")
    file.write(p[2]+ "\n\n")


# In[10]:


#TODO 2: Update the txt file by removing the first paragraph.
with open("lorem_ipsum.txt", "r") as file:
    text = file.read()


# In[11]:


paragraphs = text.split("\n\n")


# In[12]:


paragraphs 


# In[13]:


paragraphs.pop(0)


# In[14]:


paragraphs 


# In[15]:


text_sansparagraphe1 = "\n\n".join(paragraphs)


# In[16]:


with open("lorem_ipsum.txt", "w") as file:
    file.write(text_sansparagraphe1)


# In[17]:


#TODO 3: Create a dict from the paper of lecun et al. and goodfellow et al. 
#with authors, title, affiliations.


# In[27]:


paper1 = {"authors" : ["Yann LeCun", "Yoshua Bengio","Geoffrey Hinton"],
         "title" : "Deep Learning",
         "affiliation" : "Université de Montréal"}
paper2 ={"authors" : ["Ian J. Goodfellow", "Jean Pouget-Abadie", "Mehdi Mirza", "Bing Xu", "David Warde-Farley", 
                      "Sherjil Ozair", "Aaron Courville" , "Yoshua Bengio"],
          "title" : "Generative Adversarial Networks",
         "affiliation" : "Cornell University"}


# In[28]:


papers_dict = {
    "LeCun et al.": paper1,
    "Goodfellow et al.": paper2
}


# In[29]:


papers_dict


# In[22]:


#TODO 4: Save the previously created dict in the JSON format and load it back.


# In[23]:


import json


# In[30]:


with open('papers.json', 'w') as file:
    json.dump(papers_dict, file)


# In[31]:


with open('papers.json', 'r') as fp:
    test= json.load(fp)


# In[32]:


test


# In[33]:


#TODO 5: Save the previously created dict in the pickle format. 
#Try to open manually (i.e with a text editor), is it human readable ? Non 


# In[34]:


import pickle


# In[35]:


with open("papers.pickle", "wb") as file:
    pickle.dump(papers_dict, file)


# In[36]:


#TODO 6: Parse the xml_file2 in the same way as seen in the lecture:
#put infos in a dict and save it in a json file.


# In[37]:


import lxml.etree


# In[39]:


xml_file2 = "Chap2/xml_file2.nxml"
root = lxml.etree.parse(xml_file2)


# In[40]:


print(lxml.etree.tostring(root, encoding="unicode", pretty_print=True)) 


# In[43]:


date = root.xpath("//date//text()")
hour = root.xpath("//hour//text()")
recipient = root.xpath("//to//text()")
sender = root.xpath("//from//text()")
body =root.xpath("//body//text()")


# In[44]:


body


# In[45]:


info={"date":date,"hour":hour,"recipient":recipient,"sender":sender,"body":body}


# In[46]:


info


# In[47]:


with open('info.json', 'w') as file:
    json.dump(info, file)


# In[7]:


from PIL import Image
import requests


# In[8]:


#TODO 7: Download an image of your choice and save it in either jpg or png.


# In[9]:


im = Image.open(requests.get("https://img.freepik.com/photos-gratuite/happy-bunny-nombreux-oeufs-paques-herbe-fond-festif-pour-conception-decorative_90220-1091.jpg?w=740&t=st=1680470809~exp=1680471409~hmac=1a300ee77b1220227bc4436737e45288f102db19832b324f3a82ecbba2ef29b3", stream=True).raw)


# In[10]:


im


# In[12]:


im.save("bunny.png", "png")


# In[13]:


#TODO 8: From the data/Chap2/data_world.json file, create a set of publisher type.


# In[25]:


import json
with open('Chap2/data_world.json', 'r', encoding= "utf-8") as fp:
    docs= json.load(fp)


# In[26]:


docs


# In[27]:


print(docs[0].keys())


# In[28]:


for doc in (docs):
    publisher_type=(doc['publisher']['@type'])


# In[29]:


publisher_type


# In[20]:


#TODO 9: From the data/Chap2/data_world.json file,
#delete the key of your choice and save the new dict as data_world_cleaned.json.


# In[30]:


doc.pop('keyword')


# In[31]:


docs[0]


# In[32]:


with open('Chap2/data_world_cleaned.json', 'w') as fp:
    json.dump(docs, fp)


# In[ ]:




