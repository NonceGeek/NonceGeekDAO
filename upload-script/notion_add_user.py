"""
Usage:
$ python3 notion_add_user.py   \
   -n NotionTest-小明                    \
   -d 金融民工，区块链小白      \
   -g https://github.com/Demian101  \
   -i https://pic3.zhimg.com/80/v2-19797471384c0f753dcc1bedd70631ba_1440w.webp  \
   -c1 solidity  -c2 move  \
   -p1 "[智能反欺诈](https://github.com/hetrone/kesai-anti-fraud)"   \
   -p2 "[手写一个音频播放器](https://github.com/Dream4ever)"

pip3 install :
  [1] notion_client
  [2] argparse
"""

import argparse
from notion_client import Client
import os

def import_env(arg1, arg2):
    if os.path.exists('.env'):
        print('Importing environment from .env...')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            key, value = var[0].strip(), var[1].strip()
            os.environ[key] = value
    # print(os.environ.get(arg))
    return (os.environ.get(arg1), os.environ.get(arg2))


api_key, database_id = import_env("api_key", "database_id")

# Create a Notion client using the provided API key
client = Client(auth=api_key)


# Create an argument parser to parse the command line arguments
parser = argparse.ArgumentParser(description="Insert data into a Notion database")

# Add optional arguments for the database field values

parser.add_argument("-n", "--name", help="name")
parser.add_argument("-i", "--image", help="The URL of the image to insert")
parser.add_argument("-d", "--description", help="The description for the image")
parser.add_argument("-g", "--github")
parser.add_argument("-c1", "--category1")
parser.add_argument("-c2", "--category2")
parser.add_argument("-c3", "--category3")
parser.add_argument("-c4", "--category4")
parser.add_argument("-p1", "--project1")
parser.add_argument("-p2", "--project2")
parser.add_argument("-p3", "--project3")

# Parse the command line arguments
args = parser.parse_args()



def handle_multi_select_list(args):
    multi_select_list = []
    if (args.category1):
        multi_select_list.append({"name": args.category1})
    if (args.category2):
        multi_select_list.append({"name": args.category2})
    if (args.category3):
        multi_select_list.append({"name": args.category3})
    if (args.category4):
        multi_select_list.append({"name": args.category4})
    return multi_select_list

multi_select_list = handle_multi_select_list(args)

# print("multi_select_list", multi_select_list)

# Create a dictionary of field values using the provided arguments
field_values = {
    "title": {
      "title": [{ "type": "text", "text": { "content": args.name } },]
    },
    "Description":{
      "rich_text": [
      {
        "type": "text",
        "text": {
          "content": (args.description  or '')
        }
      },]
    },
    "Github":{
      "rich_text": [
      {
        "type": "text",
        "text": {
          "content": (args.github or '')
        }
      },]
    },
    "Category":{
        "multi_select": multi_select_list
    },
   
   "Image": {
     "files": [
       {
         "type": "external",
         "name": "Space Wallpaper",
         "external": {
            "url": (args.image or '')
          }
        }
      ]
    },

    "Proj1":{
      "rich_text": [
      {
        "type": "text",
        "text": {
          "content": (args.project1 or '')
        }
      },]
    },
    "Proj2":{
      "rich_text": [
      {
        "type": "text",
        "text": {
          "content": (args.project2 or '')
        }
      },]
    },
    "Proj3":{
      "rich_text": [
      {
        "type": "text",
        "text": {
          "content": (args.project3 or '')
        }
      },]
    },
}

# Insert the data into the database using the provided database ID and field values


def main():
    try:
        client.pages.create(parent={"database_id": database_id}, properties=field_values)
        print("-"*40)
        print("Insert Success!")
        print("-"*40)
    except Exception as e:
        raise
    else:
        pass
    finally:
        pass

    # Generate the documentation as a string
    help_text = parser.format_help()

    # Save the documentation to a file
    with open("Notion_API_Usage_documentation.txt", "w") as f:
        f.write(help_text)

if __name__ == '__main__':
    main()
