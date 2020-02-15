from xml.dom.minidom import parse
import xml.dom.minidom
import json
from pprint import pprint
import argparse

def parse_xml(ifile,ofile,debug=False):
    # 使用minidom解析器打开 XML 文档
    DOMTree = xml.dom.minidom.parse(ifile)
    rootNode = DOMTree.documentElement
    json_data = {}
    json_data[rootNode.nodeName] = []
    #food_list = []
 #   foods = collection.getElementsByTagName("food")
    for food in rootNode.getElementsByTagName("food"):
        fdict = {}
        for cnode in food.childNodes:
            if cnode.nodeName == '#text':
                continue
            #pprint(cnode.nodeName)
            #if cnode
            key = cnode.nodeName
            value = cnode.childNodes[0].data
            #print("current: %s : %s" % (cnode.nodeName,cnode.childNodes[0].data))
            fdict[key]=value
        json_data[rootNode.nodeName].append(fdict)
        #food_list.append(fdict)
    if debug: pprint(food_list)
    pprint(json_data)
    json.dump(json_data,open(ofile,'w'),sort_keys=True,indent=True)


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-input",type=str,required=True)
    parser.add_argument("-output",type=str,required=True)
    args = parser.parse_args()
    #if args.input:
    #    input_file = args.input
    #input_file = './xml.food'
    #output_file = './food.json'
    parse_xml(args.input,args.output)