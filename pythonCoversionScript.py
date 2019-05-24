import json
import requests
import sys
import os

headers = {
    'X-FIGMA-TOKEN': '13671-45fd49f1-ba98-4333-b317-a0f82e6094c2',
}

response = requests.get('https://api.figma.com/v1/files/Rn8xpFzATy7KbDhOwe9XS1PK', headers=headers).json()
y = json.dumps(response, indent=4)

# looping through the json data to get section data
data1 = response['document']['children'][0]['children'][0]['children']

# base variables contains the minimal base code of the mjml
base = {u'attributes': {}, u'children': [{u'attributes': {}, u'children': [{u'attributes': {u'font-size': u'', u'background-color': u''}, u'children': [], u'tagName': u'mj-container'}], u'tagName': u'mj-body'}], u'tagName': u'mjml'}
# base = {u'attributes': {}, u'children': [{u'attributes': {}, u'children': [{u'attributes': {u'background-color': u''}, u'children': [], u'tagName': u'mj-container'}], u'tagName': u'mj-body'}], u'tagName': u'mjml'}


# looping through the base dictionary to add section as a children components
output_data = base['children'][0]['children'][0]['children']



# function to triger the text section in the base file
def textSection(text_pass,text_pass2,text_pass3,text_pass4,text_pass5,color1,sc1):
    # section variable contains the base code of section
    section = {u'attributes': {u'padding-top': u'', u'background-color': u'', u'padding-bottom': u''}, u'children': [{u'attributes': {u'width': u'', u'vertical-align': u'top'}, u'tagName': u'mj-column'}], u'tagName': u'mj-section'}
    finalSection = section['children'][0]

    # text variable contains the text block to be added on base code of section
    text = [{u'content': u'', u'attributes': {u'font-size': u'', u'width': u'', u'color': u'', u'align': u'', u'padding-right': u'', u'padding-bottom': u'', u'padding-top': u'', u'font-family': u'', u'padding-left': u''}, u'tagName': u'mj-text'}]

    for k,v in section.items():
        if k == "attributes":
            for k1,v1 in section['attributes'].items():
                if k1 == "background-color":
                    section['attributes'][k1] = str(sc1)

    # for k,v in section.items():
    #     if k == "attributes":
    #         for k1,v1 in section['attributes'].items():
    #             if k1 == "background-color":
    #                 section['attributes'][k1] = str(color1)

    for key,value in text[0].items():
        if key == "content":
            text[0][key] = text_pass
        # print(key, value )
        if key == "attributes":
            for key1,value1 in text[0]['attributes'].items():
                if key1 == "font-size":
                    text[0]['attributes'][key1] = str(text_pass2) + "px"

            for key2,value2 in text[0]['attributes'].items():
                if key2 == "font-family":
                    text[0]['attributes'][key2] = text_pass3

            for key3,value3 in text[0]['attributes'].items():
                if key3 == "align":
                    text[0]['attributes'][key3] = text_pass4

            for key4,value4 in text[0]['attributes'].items():
                if key4 == "width":
                    text[0]['attributes'][key4] = str(text_pass5) + "px"

            for key5,value5 in text[0]['attributes'].items():
                if key5 == "color":
                    text[0]['attributes'][key5] = str(color1)
                    # print(color1)

    finalSection['children'] = text
    output_data.append(dict(section))

    # throwing output to final.json file
    jsonFile = open("final.json", "w+")
    jsonFile.write(json.dumps(base))
    jsonFile.close()

# function to add button section
def buttonSection(button_text,text_pass5,text_pass6,text_pass7,text_pass8,text_pass9,text_pass10,color1,sc1):
    section = {u'attributes': {u'padding-top': u'', u'background-color': u'', u'padding-bottom': u''}, u'children': [{u'attributes': {u'width': u'', u'vertical-align': u'top'}, u'tagName': u'mj-column'}], u'tagName': u'mj-section'}
    finalSection = section['children'][0]

    # block containing button base structure
    button_section = [{u'content': u'', u'height':u'', u'attributes': {u'border-radius': u'', u'width':u'', u'height':u'', u'font-size': u'', u'font-family': u'', u'color': u'', u'align': u'', u'padding': u'', u'padding-top': u'', u'background-color': u'', u'padding-left': u''}, u'tagName': u'mj-button'}]

    for k,v in section.items():
        if k == "attributes":
            for k1,v1 in section['attributes'].items():
                if k1 == "background-color":
                    section['attributes'][k1] = str(sc1)


    for key,value in button_section[0].items():
        if key == "content":
            button_section[0][key] = button_text

    for key3,value3 in button_section[0]['attributes'].items():
        if key3 == "align":
            button_section[0]['attributes'][key3] = text_pass9

    for key4,value4 in button_section[0]['attributes'].items():
        if key4 == "width":
            button_section[0]['attributes'][key4] = str(text_pass5) + "px"

    for key5,value5 in button_section[0]['attributes'].items():
        if key5 == "height":
            button_section[0]['attributes'][key5] = str(text_pass8) + "px"

    for key6,value6 in button_section[0]['attributes'].items():
        if key6 == "border-radius":
            button_section[0]['attributes'][key6] = str(text_pass10) + "px"

    for key2,value2 in button_section[0]['attributes'].items():
        if key2 == "padding-top":
            button_section[0]['attributes'][key2] = str(text_pass6) + "px"

    for key7,value7 in button_section[0]['attributes'].items():
        if key7 == "padding-left":
            button_section[0]['attributes'][key7] = str(text_pass7) + "px"

    for key8,value8 in button_section[0]['attributes'].items():
        if key8 == "color":
            button_section[0]['attributes'][key8] = str(color1)

    finalSection['children'] = button_section

    output_data.append(dict(section))

    # throwing output to final.json file
    jsonFile = open("final.json", "w+")
    jsonFile.write(json.dumps(base))
    jsonFile.close()

# function to add line segment
def lineElement(text_pass5,text_pass6,text_pass7,text_pass8,text_pass9,text_pass11,color1,sc1):

    section = {u'attributes': {u'padding-top': u'', u'background-color': u'', u'padding-bottom': u''}, u'children': [{u'attributes': {u'width': u''}, u'tagName': u'mj-column'}], u'tagName': u'mj-section'}
    finalSection = section['children'][0]

    # code block of line structure
    line = [{u'attributes': {u'border-width': u'', u'border-style': u'', u'border-color': u'', u'width': u''}, u'tagName': u'mj-divider'}]

    for k,v in section.items():
        if k == "attributes":
            for k1,v1 in section['attributes'].items():
                if k1 == "background-color":
                    section['attributes'][k1] = str(sc1)

    for key,value in line[0]['attributes'].items():
        if key == "width":
            line[0]['attributes'][key] = str(text_pass5) + "px"

    for key2,value2 in line[0]['attributes'].items():
        if key2 == "border-color":
            # print(color1)
            line[0]['attributes'][key2] = str(color1)

    for key5,value5 in line[0]['attributes'].items():
        if key5 == "border-width":
            line[0]['attributes'][key5] = str(text_pass8) + "px"

    for key6,value6 in line[0]['attributes'].items():
        if key6 == "border-style":
            line[0]['attributes'][key6] = str(text_pass11)

    for key7,value7 in line[0]['attributes'].items():
        if key7 == "padding-top":
            line[0]['attributes'][key7] = str(text_pass6) + "px"

    for key8,value8 in line[0]['attributes'].items():
        if key8 == "padding-left":
            line[0]['attributes'][key8] = str(text_pass7) + "px"

    finalSection['children'] = line
    output_data.append(dict(section))

    # json output file
    jsonFile = open("final.json", "w+")
    jsonFile.write(json.dumps(base))
    jsonFile.close()

# function to triger the element in the base file
def imageElement(src,text_pass6,text_pass7,text_pass4,text_pass5,text_pass8,text_pass9,text_pass10,text_pass11,sc1):
    section = {u'attributes': {u'padding-top': u'', u'background-color': u'', u'padding-bottom': u''}, u'children': [{u'attributes': {u'width': u'', u'vertical-align': u'top'}, u'tagName': u'mj-column'}], u'tagName': u'mj-section'}
    finalSection = section['children'][0]

    image = [{u'attributes': {u'src': u'', u'align':u'', u'width':u'', u'height':u'', u'padding-left': u'', u'padding-right': u'',u'padding-top': u'', u'padding-bottom': u'',u'border-radius': u''}, u'tagName': u'mj-image'}]

    for k,v in section.items():
        if k == "attributes":
            for k1,v1 in section['attributes'].items():
                if k1 == "background-color":
                    section['attributes'][k1] = str(sc1)

    # text1=text2=text3 = ''
    for key,value in image[0]['attributes'].items():
        if key == "src":
            # print(src)
            image[0]['attributes'][key] = str(src)

    for key2,value2 in image[0]['attributes'].items():
        if key2 == "width":
            image[0]['attributes'][key2] = str(text_pass5) + "px"

    for key3,value3 in image[0]['attributes'].items():
        if key3 == "align":
            image[0]['attributes'][key3] = text_pass9

    for key5,value5 in image[0]['attributes'].items():
        if key5 == "height":
            image[0]['attributes'][key5] = str(text_pass8) + "px"

    for key6,value6 in image[0]['attributes'].items():
        if key6 == "border-radius":
            # print(text_pass10)
            image[0]['attributes'][key6] = str(text_pass10) + "px"

    for key7,value7 in image[0]['attributes'].items():
        if key7 == "padding-top":
            # print(text_pass6)
            image[0]['attributes'][key7] = str(text_pass6) + "px"

    for key8,value8 in image[0]['attributes'].items():
        if key8 == "padding-left":
            # print(text_pass7)
            image[0]['attributes'][key8] = str(text_pass7) + "px"

    finalSection['children'] = image
    output_data.append(dict(section))

    # json output file
    jsonFile = open("final.json", "w+")
    jsonFile.write(json.dumps(base))
    jsonFile.close()

# loop for text section
text_pass = text_pass2 = text_pass3 = text_pass4 = text_pass5 = text_pass7 = text_pass8 = button_text = text_pass10 = ''
text1 = text2 = text3 = text_pass7 = text_pass13 = src=''
t1=t2=t3=sc1=color1=0
for list1 in data1:
        for key1,value1 in list1.items():
                if key1 == 'fills':
                    # print("okay")
                    for k1,v1 in list1['fills'][0]['color'].items():
                        # print(k1,v1)
                        if k1 == 'r':
                            v1 = v1 *255
                            t1 = int(v1)
                        if k1 == 'g':
                            v1 = v1 *255
                            t2 = int(v1)
                        if k1 == 'b':
                            v1 = v1 *255
                            t3 = int(v1)
                            sc1 = '#%02x%02x%02x' % (t1,t2,t3)
                            print(sc1)
                            # print(t1,t2,t3)
                # else:
                #     sc1 = color1


                if key1 == 'children':
                        for key2,value2 in value1[1].items():
                                if key2 == 'children':
                                    for k2,v2 in value1[1]['children'][0].items():
                                        # print(k2,v2)
                                        if k2 == "fills":
                                            text4=text5=text6=0
                                            for k3,v3 in value1[1]['children'][0]['fills'][0].items():
                                                if k3 == "color":
                                                    for k4,v4 in value1[1]['children'][0]['fills'][0]['color'].items():
                                                        if k4 == 'r':
                                                            v4 = v4 *255
                                                            text4 = int(v4)

                                                        if k4 == 'g':
                                                            v4 = v4 *255
                                                            text5 = int(v4)

                                                        if k4 == 'b':
                                                            v4 = v4 *255
                                                            text6 = int(v4)
                                                            color1 = '#%02x%02x%02x' % (text4, text5, text6)

                                                    # print(key2)
                                        # if k2 == "fills":
                                        #     text1=text2=text3=src =''
                                        #     for k4,v4 in value1[1]['children'][2]['fills'][0].items():
                                        #         # print(k4,v4)
                                        #         if k4 == 'imageRef':
                                        #             # print("okay")
                                        #             text_pass13 = v4
                                        #             text1 = text_pass13[:4]
                                        #             text2 = text_pass13[4:8]
                                        #             text3 = text_pass13[8:]
                                        #             # print(text1,text2,text3)
                                        #             src="https://s3-alpha-sig.figma.com/img/" + text1 + "/" + text2 + "/" + text3 + "?Expires=1559520000&Signature="


                                if key2 == 'characters':
                                    text_pass = value2

                                if key2 == 'style':
                                    for key3,value3 in value1[1]['style'].items():
                                        if key3 == 'fontSize':
                                            text_pass2 = int(value3)
                                            # print(key3,value3)

                                    for key4,value4 in value1[1]['style'].items():
                                        if key4 == 'fontFamily':
                                            text_pass3 = value4
                                            # print(key4,value4)
                                            # textSection(text_pass,text_pass2,text_pass3)

                                    for key5,value5 in value1[1]['style'].items():
                                        if key5 == 'textAlignHorizontal':
                                            text_pass4 = value5
                                            # print(key5,value5)
                                            textSection(text_pass,text_pass2,text_pass3,text_pass4,text_pass5,color1,sc1)

                                if key2 == "absoluteBoundingBox":
                                    for key6,value6 in value1[1]['absoluteBoundingBox'].items():
                                        if key6 == "width":
                                            text_pass5 = int(value6)

                                if key2 == "absoluteBoundingBox":
                                    for key7,value7 in value1[1]['absoluteBoundingBox'].items():
                                        if key7 == "y":
                                            text_pass6 = value7
                                            # print(key7,value7)

                                if key2 == "absoluteBoundingBox":
                                    for key8,value8 in value1[1]['absoluteBoundingBox'].items():
                                        if key8 == "x":
                                            test_value = value8
                                            # print("truw")
                                            if test_value < 0:
                                                text_pass7 = test_value + 600

                                            else:
                                                text_pass7 = test_value
                                                # print(text_pass7)
                                            # print(key8,text_pass7)
                                #
                                if key2 == "strokeAlign":
                                        text_pass9 = value2
                                        # print(key2,value2)

                                if key2 == "fills":
                                    text4=text5=text6=color1=0
                                    for key8,value8 in value1[1]['fills'][0].items():
                                        # print(key8,value8)
                                        if key8 == "color":
                                            for k8,v8 in value1[1]['fills'][0]['color'].items():
                                                if k8 == 'r':
                                                    v8 = v8 *255
                                                    text4 = int(v8)

                                                if k8 == 'g':
                                                    v8 = v8 *255
                                                    text5 = int(v8)

                                                if k8 == 'b':
                                                    v8 = v8 *255
                                                    text6 = int(v8)
                                                    color1 = '#%02x%02x%02x' % (text4, text5, text6)
                                                    # print(color1)
                                                    # print(text4,text5,text6)
                                #

                                if key2 == "fills":
                                    # print(key2)
                                    for key11,value11 in value1[1]['fills'][0].items():
                                        if key11 == "type":
                                            text_pass11 = value11
                                            # print(key11)

                                if key2 == "fills":
                                    # print(key2)
                                    for key11,value11 in value1[1]['fills'][0].items():
                                        if key11 == 'imageRef':
                                            text_pass13 = value11
                                            text1 = text_pass13[:4]
                                            text2 = text_pass13[4:8]
                                            text3 = text_pass13[8:]
                                            # print(text1,text2,text3)
                                            src = "https://s3-alpha-sig.figma.com/img/" + text1 + "/" + text2 + "/" + text3 + "?Expires=1559520000&Signature="
                                            imageElement(src,text_pass6,text_pass7,text_pass4,text_pass5,text_pass8,text_pass9,text_pass10,text_pass11,sc1)

                                if key2 == "cornerRadius":
                                    text_pass10 = int(value2)
                                        # print(key2,value2)
                                # "cornerRadius": 4

                                if key2 == "absoluteBoundingBox" :
                                    for key9,value9 in value1[1]['absoluteBoundingBox'].items():
                                        if key9 == "height":
                                            text_pass8 = value9
                                            # print (key9,value9)


                                if key2 == "name" and value2 == "section-hrline":
                                    lineElement(text_pass5,text_pass6,text_pass7,text_pass8,text_pass9,text_pass11,color1,sc1)

                                if key2 == "name" and value2 == "section-button-1":
                                    buttonSection(button_text,text_pass5,text_pass6,text_pass7,text_pass8,text_pass9,text_pass10,color1,sc1)

                                if key2 == "name" and value2 == "section-image":
                                    imageElement(src,text_pass6,text_pass7,text_pass4,text_pass5,text_pass8,text_pass9,text_pass10,text_pass11,sc1)



os.system("node ./node_modules/.bin/json2mjml final.json outputmjml.mjml")
os.system("mjml outputmjml.mjml -o finalhtml.html")
