import xml.etree.ElementTree as ET
import sys
#from translate import Translator
#from googletrans import Translator
from deep_translator import GoogleTranslator
from os import path

def parse(args:list) -> dict:
    result = {
        "outputPath":""
    }
    for i in range(len(args)):
        if args[i]=="-ts":
            result["tsPath"] = args[i+1]
        elif args[i]=="-target":
            result["targetLang"] = args[i+1]
        elif args[i]=="-output" or args[i]=="-o":
            result["outputPath"] = args[i+1]

    return result

if __name__ == "__main__":
    args = sys.argv
    args = parse(args)
    tree = ET.parse(args["tsPath"])
    root = tree.getroot()
    SOURCE_LANGUAGE = root.attrib["language"]
    root.attrib["language"]=args["targetLang"]

    TRANSLATOR_DEST = args["targetLang"].split("_")[0]
    TRANSLATOR_SRC = SOURCE_LANGUAGE.split("_")[0]

    translator = GoogleTranslator(source=TRANSLATOR_SRC,target=TRANSLATOR_DEST)

    for context in root.iter("context"):
        for message in context.iter("message"):
            source_text = message.find("source").text
            try:
                translated_text = translator.translate(source_text)
                print(source_text+"\t->\t"+translated_text)
                message.find("translation").text = translated_text
            except TypeError:
                continue
            

    outputPath = path.join(args["outputPath"],"translate_"+args["targetLang"])
    tree.write(outputPath,encoding="utf-8")
    print("Translated TS saved to ",outputPath)