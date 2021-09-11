#!/usr/bin/env python3
# coding=utf8
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
  "uuid": "F409FE94-5FF1-49FB-BE73-93F113186638",
  "name": "The Crawling Library",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1631398474879,
  "passages": [
    {
      "name": "The Maw of Knowledge",
      "tags": "",
      "id": "1",
	  "knowledge": 0,
	  "corruption": 0,
      "text": "In the frozen remains of a place long dead, the library makes its way through the empty wastelands. Endlessly, it wanders in search of knowledge. Hungry to add more books to its collection and fill the countless shelves that line it.\n\nIt's no wonder that so many come to the library. Not only do they come to give their knowledge to the library, but also to saciate their own lust for answers. The books of the library are open to all, so long as they can keep their mind as they wade through its twisting coradors and read through its eldritch tomes. \n\nSo, why have you come here wanderer? Do you seek the knowledge of the library?\n\n[[ENTER|The Throat of the Library]]",
      "links": [
        {
          "linkText": "ENTER",
          "passageName": "The Throat of the Library",
          "original": "[[ENTER|The Throat of the Library]]"
        }
      ],
      "hooks": [],
      "cleanText": "In the frozen remains of a place long dead, the library makes its way through the empty wastelands. Endlessly, it wanders in search of knowledge. Hungry to add more books to its collection and fill the countless shelves that line it.\n\nIt's no wonder that so many come to the library. Not only do they come to give their knowledge to the library, but also to saciate their own lust for answers. The books of the library are open to all, so long as they can keep their mind as they wade through its twisting coradors and read through its eldritch tomes. \n\nSo, why have you come here wanderer? Do you seek the knowledge of the library?"
    },
    {
      "name": "The Throat of the Library",
      "tags": "",
      "id": "2",
	  "knowledge": 0,
	  "corruption": 0,
      "text": "The doors of the library are beautifully lavish, made of delicately sculpted ivory and the interior is filled with beautiful woods. The library is kept in low light, a dim purple glow fills the rooms and your eyes eventually adjust to the new surroundings. Inside the library you see a table with a tome on it. To either side of the table are hallways, one to the left and one to the right. \n\n[[INVESTIGATE|First Tome]]\n[[RIGHT|East Hallway]]\n[[LEFT|West Hallway]]",
      "links": [
        {
          "linkText": "INVESTIGATE",
          "passageName": "First Tome",
          "original": "[[INVESTIGATE|First Tome]]"
        },
        {
          "linkText": "RIGHT",
          "passageName": "East Hallway",
          "original": "[[RIGHT|East Hallway]]"
        },
        {
          "linkText": "LEFT",
          "passageName": "West Hallway",
          "original": "[[LEFT|West Hallway]]"
        }
      ],
      "hooks": [],
      "cleanText": "The doors of the library are beautifully lavish, made of delicately sculpted ivory and the interior is filled with beautiful woods. The library is kept in low light, a dim purple glow fills the rooms and your eyes eventually adjust to the new surroundings. Inside the library you see a table with a tome on it. To either side of the table are hallways, one to the left and one to the right."
    },
    {
      "name": "First Tome",
      "tags": "",
      "id": "3",
	  "knowledge": 1,
	  "corruption": 1,
      "text": "You approach. As you near the table, the tome opens on its own. It's as if it were alive. The Pages of the tome are filled with strange letters and symbols. You can't quite make out what it says. As you flip through the pages, you fell that you have learned much but what did it cost?\n\n[[BACK|The Throat of the Library]]\n[[LEFT|West Hallway]]\n[[RIGHT|East Hallway]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "The Throat of the Library",
          "original": "[[BACK|The Throat of the Library]]"
        },
        {
          "linkText": "LEFT",
          "passageName": "West Hallway",
          "original": "[[LEFT|West Hallway]]"
        },
        {
          "linkText": "RIGHT",
          "passageName": "East Hallway",
          "original": "[[RIGHT|East Hallway]]"
        }
      ],
      "hooks": [],
      "cleanText": "You approach. As you near the table, the tome opens on its own. It's as if it were alive. The Pages of the tome are filled with strange letters and symbols. You can't quite make out what it says. As you flip through the pages, you fell that you have learned much but what did it cost?"
    },
    {
      "name": "East Hallway",
      "tags": "",
	  "knowledge": 0,
	  "corruption": 0,
      "id": "4",
      "text": "The eastern hallway is just as lavish as the entrance. Large arched colemns streach up from the floor and and converge in the spine that runs along the ceiling. Rather than the wooded pannels of the previous rooms, the walls are made of muscle, much like the outside of the library. No objects or creatures make this hallway there home, but there are two doors, one to the left and one to the right, and foreward there is some kind of gate. The gate is made of the same material as the columns, while the doors are much like the library door. \n\n[[LEFT|Writer's Corner]]\n[[RIGHT|Book Room #1]]\n[[FORWARD|Eastern Gate]]",
      "links": [
        {
          "linkText": "LEFT",
          "passageName": "Writer's Corner",
          "original": "[[LEFT|Writer's Corner]]"
        },
        {
          "linkText": "RIGHT",
          "passageName": "Book Room #1",
          "original": "[[RIGHT|Book Room #1]]"
        },
        {
          "linkText": "FORWARD",
          "passageName": "Eastern Gate",
          "original": "[[FORWARD|Eastern Gate]]"
        }
      ],
      "hooks": [],
      "cleanText": "The eastern hallway is just as lavish as the entrance. Large arched colemns streach up from the floor and and converge in the spine that runs along the ceiling. Rather than the wooded pannels of the previous rooms, the walls are made of muscle, much like the outside of the library. No objects or creatures make this hallway there home, but there are two doors, one to the left and one to the right, and foreward there is some kind of gate. The gate is made of the same material as the columns, while the doors are much like the library door."
    },
    {
      "name": "West Hallway",
      "tags": "",
      "id": "5",
	  "knowledge": 0,
	  "corruption": 0,
      "text": "The western hallway is just as lavish as the entrance. The walls are crafted of the same wooded substance as the library entrance. The floors however are mde of a hard chitin like substance. No objects or creatures make this hallway there home, but there are two doors, one to the left and one to the right, and foreward there is some kind of gate. The gate is made of the same substance as the floor, while the doors are crafted out of the materials that make up the walls. \n\n[[RIGHT|Book Room #2]] \n[[LEFT|Book Room #3]]\n[[FORWARD|Restricted Gate]]",
      "links": [
        {
          "linkText": "RIGHT",
          "passageName": "Book Room #2",
          "original": "[[RIGHT|Book Room #2]]"
        },
        {
          "linkText": "LEFT",
          "passageName": "Book Room #3",
          "original": "[[LEFT|Book Room #3]]"
        },
        {
          "linkText": "FORWARD",
          "passageName": "Restricted Gate",
          "original": "[[FORWARD|Restricted Gate]]"
        }
      ],
      "hooks": [],
      "cleanText": "The western hallway is just as lavish as the entrance. The walls are crafted of the same wooded substance as the library entrance. The floors however are mde of a hard chitin like substance. No objects or creatures make this hallway there home, but there are two doors, one to the left and one to the right, and foreward there is some kind of gate. The gate is made of the same substance as the floor, while the doors are crafted out of the materials that make up the walls."
    },
    {
      "name": "Writer's Corner",
      "tags": "",
      "id": "6",
	  "knowledge": 0,
	  "corruption": 0,
      "text": "You enter into a small room. The interior of the room is lined with muscluatur similar to the hall outside. Inside, two desk like structures sit. Their legs fused into the floor, perhaps they were grown out of the library. Its not clear if they are made of wood or bone. Each desk has on it a pen and empty pages. One of the desks is empty while the other is being used by someone.\n\n[[SPEAK|Used Desk]]\n[[INVESTIGATE|Unsued Desk]]\n[[LEAVE|East Hallway]]",
      "links": [
        {
          "linkText": "SPEAK",
          "passageName": "Used Desk",
          "original": "[[SPEAK|Used Desk]]"
        },
        {
          "linkText": "INVESTIGATE",
          "passageName": "Unsued Desk",
          "original": "[[INVESTIGATE|Unsued Desk]]"
        },
        {
          "linkText": "LEAVE",
          "passageName": "East Hallway",
          "original": "[[LEAVE|East Hallway]]"
        }
      ],
      "hooks": [],
      "cleanText": "You enter into a small room. The interior of the room is lined with muscluatur similar to the hall outside. Inside, two desk like structures sit. Their legs fused into the floor, perhaps they were grown out of the library. Its not clear if they are made of wood or bone. Each desk has on it a pen and empty pages. One of the desks is empty while the other is being used by someone."
    },
    {
      "name": "Book Room #1",
      "tags": "",
      "id": "7",
	  "knowledge": 0,
	  "corruption": 0,
      "text": "You enter into a room lined with shelves upon shelves of books. There is also a cart with books stack on it. There is a chair with someone seated at it. \n\n[[TALK|Reader]]\n[[INVESTIGATE|Book Cart]]\n[[READ|Reading]]",
      "links": [
        {
          "linkText": "TALK",
          "passageName": "Reader",
          "original": "[[TALK|Reader]]"
        },
        {
          "linkText": "INVESTIGATE",
          "passageName": "Book Cart",
          "original": "[[INVESTIGATE|Book Cart]]"
        },
        {
          "linkText": "READ",
          "passageName": "Reading",
          "original": "[[READ|Reading]]"
        }
      ],
      "hooks": [],
      "cleanText": "You enter into a room lined with shelves upon shelves of books. There is also a cart with books stack on it. There is a chair with someone seated at it."
    },
    {
      "name": "Eastern Gate",
      "tags": "",
      "id": "8",
	  "knowledge": 0,
	  "corruption": 0,
      "text": "The large skeletal gates of the eastern hall stand tall over you. Writen on the doors is an inscription. \"Historical Section\" is emblazened in runes atop the entrance. Perhaps you will find what you seek to know in here?\n\n[[PROCEED|Histroy Section]]\n[[BACK|East Hallway]]",
      "links": [
        {
          "linkText": "PROCEED",
          "passageName": "Histroy Section",
          "original": "[[PROCEED|Histroy Section]]"
        },
        {
          "linkText": "BACK",
          "passageName": "East Hallway",
          "original": "[[BACK|East Hallway]]"
        }
      ],
      "hooks": [],
      "cleanText": "The large skeletal gates of the eastern hall stand tall over you. Writen on the doors is an inscription. \"Historical Section\" is emblazened in runes atop the entrance. Perhaps you will find what you seek to know in here?"
    },
    {
      "name": "Used Desk",
      "tags": "",
      "id": "9",
	  "knowledge": 0,
	  "corruption": 1,
      "text": "You approach the person writing away at the desk. They are wearing a blackend hood, so you can't really make any details out about them. You call out to them, but they don't respond. They don't seem to notice you. It seems like they are far to enraptured with their own work, and they pay you no mind. \n\n[[LOOK|Writer]]\n[[LEAVE|Writer's Corner]]",
      "links": [
        {
          "linkText": "LOOK",
          "passageName": "Writer",
          "original": "[[LOOK|Writer]]"
        },
        {
          "linkText": "LEAVE",
          "passageName": "Writer's Corner",
          "original": "[[LEAVE|Writer's Corner]]"
        }
      ],
      "hooks": [],
      "cleanText": "You approach the person writing away at the desk. They are wearing a blackend hood, so you can't really make any details out about them. You call out to them, but they don't respond. They don't seem to notice you. It seems like they are far to enraptured with their own work, and they pay you no mind."
    },
    {
      "name": "Unsued Desk",
      "tags": "",
      "id": "10",
	  "knowledge": 1,
	  "corruption": 2,
      "text": "You approach the unused desk. The desk has no chair to sit at. Upon further inspection, the desk seems quite detailed, with filigree and fringes. The pen and pages sit empty atop the structure. They are tantalizing, empty and waiting to be filled out. Perhaps you could write something. Is there anything you want to write down?\n\n[[WRITE|Writing]]\n[[LEAVE|Writer's Corner]]",
      "links": [
        {
          "linkText": "WRITE",
          "passageName": "Writing",
          "original": "[[WRITE|Writing]]"
        },
        {
          "linkText": "LEAVE|Writer's Corner",
          "passageName": "LEAVE|Writer's Corner",
          "original": "[[LEAVE|Writer's Corner]]"
        }
      ],
      "hooks": [],
      "cleanText": "You approach the unused desk. The desk has no chair to sit at. Upon further inspection, the desk seems quite detailed, with filigree and fringes. The pen and pages sit empty atop the structure. They are tantalizing, empty and waiting to be filled out. Perhaps you could write something. Is there anything you want to write down?"
    },
    {
      "name": "Writer",
      "tags": "",
      "id": "11",
	  "knowledge": 3,
	  "corruption": 5,
      "text": "You look upon the writings of the hooded figure. As you lean close you can see an exposed, cow like skull that is visible just under the ragged flesh they have drapped over themself. The pen they hold has fully fused into their hand. You gaze upon the unsightly writings of the creature. It hurts your mind to mearly gaze upon it, but its hard to look away. You only have a breif look, but you have already learned so much from this creature.\n\n[[BACK|Writer's Corner]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Writer's Corner",
          "original": "[[BACK|Writer's Corner]]"
        }
      ],
      "hooks": [],
      "cleanText": "You look upon the writings of the hooded figure. As you lean close you can see an exposed, cow like skull that is visible just under the ragged flesh they have drapped over themself. The pen they hold has fully fused into their hand. You gaze upon the unsightly writings of the creature. It hurts your mind to mearly gaze upon it, but its hard to look away. You only have a breif look, but you have already learned so much from this creature."
    },
    {
      "name": "Writing",
      "tags": "",
      "id": "12",
	  "knowledge": 5,
	  "corruption": 10,
      "text": "You deside to write something down. You take up the pen and start to fill out one of the empty pages. As you start to write, you start to feel better about yourself, having done some good and added to the library. You ended up filling a whole page, but maybe you could write some more. Just one page? that can't be enough. No, no, you must keep going. You can't help yourself really. You just have to...\n\nYou end up filling another page...\n\nbut its still just not enough, you can't help but write and write. Now that you've started writing, you don't think you can stop. Not that you want to.\n\n[[END|The End]]",
      "links": [
        {
          "linkText": "END",
          "passageName": "The End",
          "original": "[[END|The End]]"
        }
      ],
      "hooks": [],
      "cleanText": "You deside to write something down. You take up the pen and start to fill out one of the empty pages. As you start to write, you start to feel better about yourself, having done some good and added to the library. You ended up filling a whole page, but maybe you could write some more. Just one page? that can't be enough. No, no, you must keep going. You can't help yourself really. You just have to...\n\nYou end up filling another page...\n\nbut its still just not enough, you can't help but write and write. Now that you've started writing, you don't think you can stop. Not that you want to."
    },
    {
      "name": "The End",
      "tags": "",
      "id": "13",
	  "knowledge": 0,
	  "corruption": 0,
      "text": "You have become a part of the library. It what was meant to hapen, and we librarians accept you into our ranks with open arms. There's never enough of us filling out books and organizing all the books. Hopefully you will enjoy your time with us. Was there anything you missed? Would you like to relive your experience and reminesee about your first day in the library.\n\n[[AGAIN|The Maw of Knowledge]]",
      "links": [
        {
          "linkText": "AGAIN",
          "passageName": "The Maw of Knowledge",
          "original": "[[AGAIN|The Maw of Knowledge]]"
        }
      ],
      "hooks": [],
      "cleanText": "You have become a part of the library. It what was meant to hapen, and we librarians accept you into our ranks with open arms. There's never enough of us filling out books and organizing all the books. Hopefully you will enjoy your time with us. Was there anything you missed? Would you like to relive your experience and reminesee about your first day in the library."
    },
    {
      "name": "Reader",
      "tags": "",
      "id": "14",
	  "knowledge": 2,
	  "corruption": 3,
      "text": "You approach the person reading. They are a twisted creature, fused into the chair that they are reading from. Their fleshy bulbous head is covered in many eyes, each one focused intensely on the book they have gripped in their talon like fingers. You call out to them, but they don't reply. They seem enraptured by the texts. \n\n[[READ|Reading]] \n[[LEAVE|Book Room #1]]",
      "links": [
        {
          "linkText": "READ",
          "passageName": "Reading",
          "original": "[[READ|Reading]]"
        },
        {
          "linkText": "LEAVE",
          "passageName": "Book Room #1",
          "original": "[[LEAVE|Book Room #1]]"
        }
      ],
      "hooks": [],
      "cleanText": "You approach the person reading. They are a twisted creature, fused into the chair that they are reading from. Their fleshy bulbous head is covered in many eyes, each one focused intensely on the book they have gripped in their talon like fingers. You call out to them, but they don't reply. They seem enraptured by the texts."
    },
    {
      "name": "Book Cart",
      "tags": "",
      "id": "15",
	  "knowledge": 0,
	  "corruption": 0,
      "text": "The two tiered book card is piled high with books. The poor things little legs seem like they're giving out from the strain of all the heavy books that its carring on its back. You wonder why its gone so long without any librarians coming to give it a hand. It doesn't seem like its supposed to put the books away autonomously, it has no arms with which to acomplish such a task.\n\n[[HELP|Put away books]]\n[[LEAVE|Book Room #1]]",
      "links": [
        {
          "linkText": "HELP",
          "passageName": "Put away books",
          "original": "[[HELP|Put away books]]"
        },
        {
          "linkText": "LEAVE",
          "passageName": "Book Room #1",
          "original": "[[LEAVE|Book Room #1]]"
        }
      ],
      "hooks": [],
      "cleanText": "The two tiered book card is piled high with books. The poor things little legs seem like they're giving out from the strain of all the heavy books that its carring on its back. You wonder why its gone so long without any librarians coming to give it a hand. It doesn't seem like its supposed to put the books away autonomously, it has no arms with which to acomplish such a task."
    },
    {
      "name": "Reading",
      "tags": "",
      "id": "16",
	  "knowledge": 5,
	  "corruption": 3,
      "text": "You take some time to read some books of the books. They are quite interesting, you learn much about the world, though none tell you exactly what you want to know.\n\n[[BACK|Book Room #1]]",
      "links": [
        {
          "linkText": "BACK",
          "passageName": "Book Room #1",
          "original": "[[BACK|Book Room #1]]"
        }
      ],
      "hooks": [],
      "cleanText": "You take some time to read some books of the books. They are quite interesting, you learn much about the world, though none tell you exactly what you want to know."
    },
    {
      "name": "Put away books",
      "tags": "",
      "id": "17",
	  "knowledge": 2,
	  "corruption": 10,
      "text": "You take up some of the books from the cart and move them back onto the shelves. It feels quite nice to give back to the library. As you continue to put away books, you can't help but loose track of time. It just so much fun organizing all the books along the walls. By the time you finish putting away books, you've wandered into another room. You're not quite sure where you are now...\n\nYou look to the cart, you've grown attatched to it. You can't just abandon it here can you? It seems to have found more books to put away. Maybe you could do one more round with him, it couldn't hurt...\n\n[[END|The End]]",
      "links": [
        {
          "linkText": "END",
          "passageName": "The End",
          "original": "[[END|The End]]"
        }
      ],
      "hooks": [],
      "cleanText": "You take up some of the books from the cart and move them back onto the shelves. It feels quite nice to give back to the library. As you continue to put away books, you can't help but loose track of time. It just so much fun organizing all the books along the walls. By the time you finish putting away books, you've wandered into another room. You're not quite sure where you are now...\n\nYou look to the cart, you've grown attatched to it. You can't just abandon it here can you? It seems to have found more books to put away. Maybe you could do one more round with him, it couldn't hurt..."
    },
    {
      "name": "Histroy Section",
      "tags": "",
      "id": "18",
	  "knowledge": 2,
	  "corruption": 2,
      "text": "As you enter through the gate, you come inside a massive room. Massive towers of chitan are erected into the air, each one filled to the brim with books. Towering spires of knowledge rise from the floor in colemns of bone, they reach all the way to the ceiling. Their massive presence is awe-inspiring. Amongst the countless spires and books that line the enormous room, you see one of the librarians. There is also a particular book on display. A glowing puppa casting it irridesense over the tome, making it stand out against the blackend chitin of the floor and the white spires of bone. \n\n[[TALK|The Librarian]]\n[[READ|The Ancient Texts]]",
      "links": [
        {
          "linkText": "TALK",
          "passageName": "The Librarian",
          "original": "[[TALK|The Librarian]]"
        },
        {
          "linkText": "READ",
          "passageName": "The Ancient Texts",
          "original": "[[READ|The Ancient Texts]]"
        }
      ],
      "hooks": [],
      "cleanText": "As you enter through the gate, you come inside a massive room. Massive towers of chitan are erected into the air, each one filled to the brim with books. Towering spires of knowledge rise from the floor in colemns of bone, they reach all the way to the ceiling. Their massive presence is awe-inspiring. Amongst the countless spires and books that line the enormous room, you see one of the librarians. There is also a particular book on display. A glowing puppa casting it irridesense over the tome, making it stand out against the blackend chitin of the floor and the white spires of bone."
    },
    {
      "name": "The Librarian",
      "tags": "",
      "id": "19",
	  "knowledge": 2,
	  "corruption": 0,
      "text": "You approach the libarian. With your eyes more adjusted to the darkness, you are able to make out the details of the librarian. They are elivated on a snake like tail, formed of muscle but without scales, they have six claws of decreasing size with which they hold books and two long tendrils with which they adjust and move the books along the shelves. Seven eyes dot their face and a mass of writhing tentacles hange down over where their mouth should be. \n\nYou call out to the librarian. They turn to you, and speak.\n\n[[CONTINUE|Conversation Part 1]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "Conversation Part 1",
          "original": "[[CONTINUE|Conversation Part 1]]"
        }
      ],
      "hooks": [],
      "cleanText": "You approach the libarian. With your eyes more adjusted to the darkness, you are able to make out the details of the librarian. They are elivated on a snake like tail, formed of muscle but without scales, they have six claws of decreasing size with which they hold books and two long tendrils with which they adjust and move the books along the shelves. Seven eyes dot their face and a mass of writhing tentacles hange down over where their mouth should be. \n\nYou call out to the librarian. They turn to you, and speak."
    },
    {
      "name": "The Ancient Texts",
      "tags": "",
      "id": "20",
	  "knowledge": 10,
	  "corruption": 10,
      "text": "\"Long ago, there were once a species known as the T̶̛̺̗͍̤̒̎̅̒ͅh̵̛͕͚̲͑͘ě̴̻̬ ̵͉̦̖̍̓̈́̀Ṍ̵̭l̸͔̬͐̌̐̕d̴̤͋͑ ̷̧̀O̵̦̞͝ṉ̴̝́̂́́͑ȩ̵̛͔͎͈̻̃̎s̴̨͙̀̈͋̕. They were masters of life, able to create life from nothing but muck. The key to their power was the mystical elixer, Ichor. They could command ichor in ways that we can only imagine. Their ability to craft species like clay makes our homunculi look like child's play.\"\n\n[[CONTINUE|Text Part 2]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "Text Part 2",
          "original": "[[CONTINUE|Text Part 2]]"
        }
      ],
      "hooks": [],
      "cleanText": "\"Long ago, there were once a species known as the T̶̛̺̗͍̤̒̎̅̒ͅh̵̛͕͚̲͑͘ě̴̻̬ ̵͉̦̖̍̓̈́̀Ṍ̵̭l̸͔̬͐̌̐̕d̴̤͋͑ ̷̧̀O̵̦̞͝ṉ̴̝́̂́́͑ȩ̵̛͔͎͈̻̃̎s̴̨͙̀̈͋̕. They were masters of life, able to create life from nothing but muck. The key to their power was the mystical elixer, Ichor. They could command ichor in ways that we can only imagine. Their ability to craft species like clay makes our homunculi look like child's play.\""
    },
    {
      "name": "Conversation Part 1",
      "tags": "",
      "id": "21",
	  "knowledge": 2,
	  "corruption": 1,
      "text": "\"Greetings wanderer\" The librarian says. \"Why have you come to the library? Is there something you wish to know?\"\n\n[[SPEAK|Conversation Part 2]]\n[[LEAVE|Conversation End]]",
      "links": [
        {
          "linkText": "SPEAK",
          "passageName": "Conversation Part 2",
          "original": "[[SPEAK|Conversation Part 2]]"
        },
        {
          "linkText": "LEAVE",
          "passageName": "Conversation End",
          "original": "[[LEAVE|Conversation End]]"
        }
      ],
      "hooks": [],
      "cleanText": "\"Greetings wanderer\" The librarian says. \"Why have you come to the library? Is there something you wish to know?\""
    },
    {
      "name": "Conversation Part 2",
      "tags": "",
      "id": "22",
	  "knowledge": 3,
	  "corruption": 2,
      "text": "You tell the librarian that which you seak.\n\n\"Ah, I see,\" They say. They think for a moment. \"I can grant you the information you seek.\" They turn away from you and say, \"Follow me traveler, and I will bring you to the answers that you desire.\" They walk away from you a distance and wait for you to follow.\n\n[[FOLLOW|Conversation Part 3]]\n[[LEAVE|Conversation End]]",
      "links": [
        {
          "linkText": "FOLLOW",
          "passageName": "Conversation Part 3",
          "original": "[[FOLLOW|Conversation Part 3]]"
        },
        {
          "linkText": "LEAVE",
          "passageName": "Conversation End",
          "original": "[[LEAVE|Conversation End]]"
        }
      ],
      "hooks": [],
      "cleanText": "You tell the librarian that which you seak.\n\n\"Ah, I see,\" They say. They think for a moment. \"I can grant you the information you seek.\" They turn away from you and say, \"Follow me traveler, and I will bring you to the answers that you desire.\" They walk away from you a distance and wait for you to follow."
    },
    {
      "name": "Conversation End",
      "tags": "",
      "id": "23",
	  "knowledge": 0,
	  "corruption": 0,
      "text": "As you leave, you see the Librarian turn back to his work, paying you no mind.\n\n[[CONTINUE|Histroy Section]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "Histroy Section",
          "original": "[[CONTINUE|Histroy Section]]"
        }
      ],
      "hooks": [],
      "cleanText": "As you leave, you see the Librarian turn back to his work, paying you no mind."
    },
    {
      "name": "Conversation Part 3",
      "tags": "",
      "id": "24",
	  "knowledge": 0,
	  "corruption": 0,
      "text": "You follow the librarian through the many halls of the History section before arriving at their destination. \n\n\"Here we are,\" they state. \"Here you will find what you wish to know.\"\n\nBefore you lays a massive scroll. It hangs from the ceiling and spills over the floor. It is whethered and old, decrepid in appearance when compared to the beautiful and pristeen texts that surround it. \n\nYou approach the scroll as the librarian leaves you to your research.\n\n[[READ|The Scroll]]\n[[LEAVE|No turning back]]",
      "links": [
        {
          "linkText": "READ",
          "passageName": "The Scroll",
          "original": "[[READ|The Scroll]]"
        },
        {
          "linkText": "LEAVE",
          "passageName": "No turning back",
          "original": "[[LEAVE|No turning back]]"
        }
      ],
      "hooks": [],
      "cleanText": "You follow the librarian through the many halls of the History section before arriving at their destination. \n\n\"Here we are,\" they state. \"Here you will find what you wish to know.\"\n\nBefore you lays a massive scroll. It hangs from the ceiling and spills over the floor. It is whethered and old, decrepid in appearance when compared to the beautiful and pristeen texts that surround it. \n\nYou approach the scroll as the librarian leaves you to your research."
    },
    {
      "name": "The Scroll",
      "tags": "",
      "id": "25",
	  "knowledge": 1,
	  "corruption": 1,
      "text": "You approach the scroll, its bountful knowledge becons to you, inviting you to read from it.\n\n[[BEGIN|True Knowledge]]\n[[LEAVE|No turning back]]",
      "links": [
        {
          "linkText": "BEGIN",
          "passageName": "True Knowledge",
          "original": "[[BEGIN|True Knowledge]]"
        },
        {
          "linkText": "LEAVE",
          "passageName": "No turning back",
          "original": "[[LEAVE|No turning back]]"
        }
      ],
      "hooks": [],
      "cleanText": "You approach the scroll, its bountful knowledge becons to you, inviting you to read from it."
    },
    {
      "name": "No turning back",
      "tags": "",
      "id": "26",
	  "knowledge": 0,
	  "corruption": 0,
      "text": "With your goal so clearly in view? There's no way you could simply give up now. You must continue! You must grasp your goal!\n\n[[CONTINUE|The Scroll]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "The Scroll",
          "original": "[[CONTINUE|The Scroll]]"
        }
      ],
      "hooks": [],
      "cleanText": "With your goal so clearly in view? There's no way you could simply give up now. You must continue! You must grasp your goal!"
    },
    {
      "name": "True Knowledge",
      "tags": "",
      "id": "27",
	  "knowledge": 30,
	  "corruption": 30,
      "text": "\"Why do we write? I have asked myself this question on many occasions. Why do we humans lust for knowledge. It is our express purpose to grow and to learn. I think that this reason is why we write. As a way of proving that we have this knowledge. It is a way of proving knowlegde. In the same way that the beasts prove their strength by scatering corpses around their domain. We prove our strength of mind by parading around the words which we have etched into bones and carved into flesh. I think that it is noble in that way. In the primal way that it is noble for the strongest beast to sit at the top of the food chain, it is noble for us to hold knowledge and express it. It is a primal part of us. A very core part of our being. That is why I hoard knowledge. If I were to explain why I collect books and hold them so close to my heart. I do not think I can be parted from this, from this hunger to learn and know. That is why I wander. I seek to have more knowledge and I seek to hold it over others. To lord over them as to prove that I am the strongest of mind. Perhaps it is too simple a motivation, but life is quite simple. If you think about it.\"\n- Excerpt from the scroll\n\n\n[[CONTINUE|A goal reached]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "A goal reached",
          "original": "[[CONTINUE|A goal reached]]"
        }
      ],
      "hooks": [],
      "cleanText": "\"Why do we write? I have asked myself this question on many occasions. Why do we humans lust for knowledge. It is our express purpose to grow and to learn. I think that this reason is why we write. As a way of proving that we have this knowledge. It is a way of proving knowlegde. In the same way that the beasts prove their strength by scatering corpses around their domain. We prove our strength of mind by parading around the words which we have etched into bones and carved into flesh. I think that it is noble in that way. In the primal way that it is noble for the strongest beast to sit at the top of the food chain, it is noble for us to hold knowledge and express it. It is a primal part of us. A very core part of our being. That is why I hoard knowledge. If I were to explain why I collect books and hold them so close to my heart. I do not think I can be parted from this, from this hunger to learn and know. That is why I wander. I seek to have more knowledge and I seek to hold it over others. To lord over them as to prove that I am the strongest of mind. Perhaps it is too simple a motivation, but life is quite simple. If you think about it.\"\n- Excerpt from the scroll"
    },
    {
      "name": "A goal reached",
      "tags": "",
      "id": "28",
	  "knowledge": 0,
	  "corruption": 0,
      "text": "You have done it, you have learned the thing that you wished to know. But is it enough for you? Perhaps you have more reading to do, before you are truely sacisfied. Maybe you should stay in the Library and read more.\n\n[[END|The End]]",
      "links": [
        {
          "linkText": "END",
          "passageName": "The End",
          "original": "[[END|The End]]"
        }
      ],
      "hooks": [],
      "cleanText": "You have done it, you have learned the thing that you wished to know. But is it enough for you? Perhaps you have more reading to do, before you are truely sacisfied. Maybe you should stay in the Library and read more."
    },
    {
      "name": "Text Part 2",
      "tags": "",
      "id": "29",
	  "knowledge": 10,
	  "corruption": 10, 
      "text": "\"T̷̡͇̭̘̘̑ḫ̴̢͚̠͙̟̭̃̆̒̈́̂̓͠e̸̦͈͋̉͗͗͝ ̷͖̋͆̉͌̈́̉͆̎̂̀O̵̥̱̯̥̼̻̼̊̓͒̽͛̒̑̊͜͝͝ͅl̶̝̩͔͕̦̩̈́̑̀́̌́͌͋̈̇̊ͅd̵̨̦͎̫̖̗͔̳̟̀̍͋́̈́̎̚͠͠͝͝ ̷̧̨̦̙͖̜͇̈́̏̆́̈́͘͝Ớ̴̫̤͈̟̲̹͘͠n̴̫͙̪̼̭͔̽̈̀e̸̢͈̩͕̼͚̺̿͌̅̇̉s̸̲̰̅̿̓̓́̾̉̀  would eventually fall. It is unkown what would cause T̷̨̟̞̩̲̓̊͋̓̌̆́͂̕h̵̪̩͈͉͔͕͙͎͇̤̩̋̀̒̈́̀̍̔̐e̵̺̹̣̦̬͙͈̺̝̲̟̠͛͂͘͜͝ ̴̼͈͉̈́Ǫ̸͋̅́̀̊̍̈́͒̽͝͠l̷̜̭͕̻̔͐̍́̇́́́ͅd̴̩̗͚̝̤̙̣̰̫̆̑̄̐͊͛́͌̌̌̀̌ ̸̛̩͓̜͓̭̾̽̄͑̀̃̀͑͆͊͜O̸̡̤̻̮̫͓̗̼͖̭̫̒n̴̡̠̤̞̘̬̮͖̥̩͓̉̅e̷̢̧̧͔͙̝̙͔̼̮̽͒́́̎̐͑̓̓̚͝͝s̴̹͇̖͔͔̫̱̖͚̳̺̺͛̄̎̈́͆͐͑̕͝  to lose their empire, but it would end none the less. Eventually humanity would find the remants of their empires among the ruins of T̴͔͓̠͔̟̠͓̊́̌o̷̮̼̔́̊w̶̭̒̔̌̏̀̈́̾͒̈́̚͝͝e̸̛̛̦͖̯̝̺̪͚̹͈̗͕̩̝͆͒̉̇͋́̆̄̊̀̌́̐ͅr̶̡̧̜͓̣͕̰͙͙͐̅́̾͜ ̵̨̨̳͈͚̦̮̝͍̼͈͑̾̉͝o̵̢̧̡̳̪̰̝͔̭͍͔̘̜̲̊̔͊̈́̐͛f̵̝̺̻̳̼̟̗̺̙͉̙̖̬̦̖͒̉̋͒̈̆́́̀̈́̓͂̋ ̸̝͉͖̮̪̜̬̳͔̝̫̓̉̉͂̈̾͜G̴̡͖̘̺̠̣̘̰̖̫̈̉͌͂̈́́͋̑̈́̃̈́ͅo̷̢̨̦̮̤̭̩̩̫̟͖̜̙̬̿ͅḏ̸͓̩̠̩͍̼̦̣̺̠̹͈͜͝ . This would be how humanity would discover Ichor. It would be their first takes of true power. \n\n[[CONTINUE|Text Part 3]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "Text Part 3",
          "original": "[[CONTINUE|Text Part 3]]"
        }
      ],
      "hooks": [],
      "cleanText": "\"T̷̡͇̭̘̘̑ḫ̴̢͚̠͙̟̭̃̆̒̈́̂̓͠e̸̦͈͋̉͗͗͝ ̷͖̋͆̉͌̈́̉͆̎̂̀O̵̥̱̯̥̼̻̼̊̓͒̽͛̒̑̊͜͝͝ͅl̶̝̩͔͕̦̩̈́̑̀́̌́͌͋̈̇̊ͅd̵̨̦͎̫̖̗͔̳̟̀̍͋́̈́̎̚͠͠͝͝ ̷̧̨̦̙͖̜͇̈́̏̆́̈́͘͝Ớ̴̫̤͈̟̲̹͘͠n̴̫͙̪̼̭͔̽̈̀e̸̢͈̩͕̼͚̺̿͌̅̇̉s̸̲̰̅̿̓̓́̾̉̀  would eventually fall. It is unkown what would cause T̷̨̟̞̩̲̓̊͋̓̌̆́͂̕h̵̪̩͈͉͔͕͙͎͇̤̩̋̀̒̈́̀̍̔̐e̵̺̹̣̦̬͙͈̺̝̲̟̠͛͂͘͜͝ ̴̼͈͉̈́Ǫ̸͋̅́̀̊̍̈́͒̽͝͠l̷̜̭͕̻̔͐̍́̇́́́ͅd̴̩̗͚̝̤̙̣̰̫̆̑̄̐͊͛́͌̌̌̀̌ ̸̛̩͓̜͓̭̾̽̄͑̀̃̀͑͆͊͜O̸̡̤̻̮̫͓̗̼͖̭̫̒n̴̡̠̤̞̘̬̮͖̥̩͓̉̅e̷̢̧̧͔͙̝̙͔̼̮̽͒́́̎̐͑̓̓̚͝͝s̴̹͇̖͔͔̫̱̖͚̳̺̺͛̄̎̈́͆͐͑̕͝  to lose their empire, but it would end none the less. Eventually humanity would find the remants of their empires among the ruins of T̴͔͓̠͔̟̠͓̊́̌o̷̮̼̔́̊w̶̭̒̔̌̏̀̈́̾͒̈́̚͝͝e̸̛̛̦͖̯̝̺̪͚̹͈̗͕̩̝͆͒̉̇͋́̆̄̊̀̌́̐ͅr̶̡̧̜͓̣͕̰͙͙͐̅́̾͜ ̵̨̨̳͈͚̦̮̝͍̼͈͑̾̉͝o̵̢̧̡̳̪̰̝͔̭͍͔̘̜̲̊̔͊̈́̐͛f̵̝̺̻̳̼̟̗̺̙͉̙̖̬̦̖͒̉̋͒̈̆́́̀̈́̓͂̋ ̸̝͉͖̮̪̜̬̳͔̝̫̓̉̉͂̈̾͜G̴̡͖̘̺̠̣̘̰̖̫̈̉͌͂̈́́͋̑̈́̃̈́ͅo̷̢̨̦̮̤̭̩̩̫̟͖̜̙̬̿ͅḏ̸͓̩̠̩͍̼̦̣̺̠̹͈͜͝ . This would be how humanity would discover Ichor. It would be their first takes of true power."
    },
    {
      "name": "Text Part 3",
      "tags": "",
      "id": "30",
	  "knowledge": 10,
	  "corruption": 10,
      "text": "T̶̼̚ḫ̶̈ị̷̿s̸̺̚ ̶̱̈́w̸͈̃o̴̺̅u̷̻͌l̷̼̈d̵͈̽ ̶̖͠i̸̠͠n̶̜͛è̷̖v̸̪͌i̷̼͑t̶͇͌à̵͈b̴̳͘ḷ̴̽y̷̡̎ ̸̱̌d̴̺̉r̴̜͋i̷̞̋v̴̪͗ě̸̟ ̸̳̕h̵̛ͅu̸͖̒ṃ̵̄a̷̜̚ñ̴͎i̶̛̝t̶̗̓y̷̗̚ ̸͇̄ṱ̴̾ȏ̷̧ ̸̼͘ẅ̸̺́ä̴͕́r̸̲͂.̷̳͋ ̴̨̉T̵̹̀h̸͓͝e̷̗͠i̵̫͂r̵̲̈́ ̴̢͒m̵̭͘a̸͉̿k̴̡̅ḛ̴̌ ̴̟͑ḅ̸̇e̴̢͌l̴̙̑i̷̯̊ȇ̸̢v̶̡͋ê̴̖ ̶̤͂s̴̥͋ǫ̵̇c̵̱̓ȉ̵͜ȇ̴͓t̸͓̉y̵̼͛ ̴̠̽w̶͚͆a̵̢͐ṡ̵̮ ̵̦̈́n̶̬͗o̶̱͋ ̵͚̆m̷͔̎a̸̮͠t̸̨̽c̶͙̒ḣ̴̠ ̴̦̚ẃ̸̳h̸̞̋ȇ̸̫n̴̥̑ ̷̲͘p̸͚̓ṷ̵̄ṱ̴̓ ̴̱́i̸̺̔n̶̻̍ ̴̤̎c̶͈͒o̸̡̎n̵̲̒t̵͎̚r̵͔̉a̷͚͌s̸̡̔ẗ̴̬́ ̵̹͒w̸̯̕i̴̞̎t̸̛͓h̸͓̐ ̸͍͛t̴̤͝ḧ̶͚́e̷̯͠î̴̜r̸͆ͅ ̸̯̿p̸̧̅r̷̫͐ì̸͉m̶̀͜à̵̻l̷̓ͅ ̶͔̽n̷̹͐e̴͙͗ę̶͊d̴̹̍ ̵̠̏f̶̻͊o̸̙̾r̸͚̀ ̶̳̓ṗ̸͔ơ̴̘w̷̘͌ẹ̸͂ŕ̴̤.̴̠̀ ̴̯̄T̵̡͂h̵̡̃e̸̫͂ ̶̹̓h̸̼̾u̶̖̅m̶͙̄a̶̠͠ñ̶̤ș̷̚ ̸̜̑t̵̒͜o̶̻̍r̶̙̋e̶̢̋ ̷̨̌t̶̞̔h̷̼͌e̵͍͂m̴͔͋ŝ̸̞e̸̞̅l̶̩̇v̶̳̋e̴͔̓s̸̗͂ ̶̯̆t̴͖̿ò̵͓ ̴̜͑s̸͓̈́h̸̻̒r̶̪̂e̷̠͐a̵̩̽d̶͕̅s̷̼̀ ̸̠̚ẗ̴̨ř̵̨y̸̥͐i̸̬̕ṉ̸̅g̶͇͝ ̶̪́t̴̰̚o̵̊͜ ̵̹̈́s̴̟̍ė̷̥c̷͔̓u̵͚͠r̵͔̅e̷͇͊ ̵̯̇t̵̤̑h̵̯͐ė̵͇ ̴̰̊i̷̫̒c̸̖̀o̵̔ͅȑ̶̮ḙ̵̑ ̵̗̑f̵͉̈ó̸̱r̵̛̘ ̵͍̓ṫ̴̝h̷͙̒e̷̞͒ṁ̸̨s̸̡͘ę̴̾ĺ̸̠v̴͙̒ḙ̶̒s̵̹̀.̴̠͒/. \n\n[[CONTINUE|Text Part 4]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "Text Part 4",
          "original": "[[CONTINUE|Text Part 4]]"
        }
      ],
      "hooks": [],
      "cleanText": "T̶̼̚ḫ̶̈ị̷̿s̸̺̚ ̶̱̈́w̸͈̃o̴̺̅u̷̻͌l̷̼̈d̵͈̽ ̶̖͠i̸̠͠n̶̜͛è̷̖v̸̪͌i̷̼͑t̶͇͌à̵͈b̴̳͘ḷ̴̽y̷̡̎ ̸̱̌d̴̺̉r̴̜͋i̷̞̋v̴̪͗ě̸̟ ̸̳̕h̵̛ͅu̸͖̒ṃ̵̄a̷̜̚ñ̴͎i̶̛̝t̶̗̓y̷̗̚ ̸͇̄ṱ̴̾ȏ̷̧ ̸̼͘ẅ̸̺́ä̴͕́r̸̲͂.̷̳͋ ̴̨̉T̵̹̀h̸͓͝e̷̗͠i̵̫͂r̵̲̈́ ̴̢͒m̵̭͘a̸͉̿k̴̡̅ḛ̴̌ ̴̟͑ḅ̸̇e̴̢͌l̴̙̑i̷̯̊ȇ̸̢v̶̡͋ê̴̖ ̶̤͂s̴̥͋ǫ̵̇c̵̱̓ȉ̵͜ȇ̴͓t̸͓̉y̵̼͛ ̴̠̽w̶͚͆a̵̢͐ṡ̵̮ ̵̦̈́n̶̬͗o̶̱͋ ̵͚̆m̷͔̎a̸̮͠t̸̨̽c̶͙̒ḣ̴̠ ̴̦̚ẃ̸̳h̸̞̋ȇ̸̫n̴̥̑ ̷̲͘p̸͚̓ṷ̵̄ṱ̴̓ ̴̱́i̸̺̔n̶̻̍ ̴̤̎c̶͈͒o̸̡̎n̵̲̒t̵͎̚r̵͔̉a̷͚͌s̸̡̔ẗ̴̬́ ̵̹͒w̸̯̕i̴̞̎t̸̛͓h̸͓̐ ̸͍͛t̴̤͝ḧ̶͚́e̷̯͠î̴̜r̸͆ͅ ̸̯̿p̸̧̅r̷̫͐ì̸͉m̶̀͜à̵̻l̷̓ͅ ̶͔̽n̷̹͐e̴͙͗ę̶͊d̴̹̍ ̵̠̏f̶̻͊o̸̙̾r̸͚̀ ̶̳̓ṗ̸͔ơ̴̘w̷̘͌ẹ̸͂ŕ̴̤.̴̠̀ ̴̯̄T̵̡͂h̵̡̃e̸̫͂ ̶̹̓h̸̼̾u̶̖̅m̶͙̄a̶̠͠ñ̶̤ș̷̚ ̸̜̑t̵̒͜o̶̻̍r̶̙̋e̶̢̋ ̷̨̌t̶̞̔h̷̼͌e̵͍͂m̴͔͋ŝ̸̞e̸̞̅l̶̩̇v̶̳̋e̴͔̓s̸̗͂ ̶̯̆t̴͖̿ò̵͓ ̴̜͑s̸͓̈́h̸̻̒r̶̪̂e̷̠͐a̵̩̽d̶͕̅s̷̼̀ ̸̠̚ẗ̴̨ř̵̨y̸̥͐i̸̬̕ṉ̸̅g̶͇͝ ̶̪́t̴̰̚o̵̊͜ ̵̹̈́s̴̟̍ė̷̥c̷͔̓u̵͚͠r̵͔̅e̷͇͊ ̵̯̇t̵̤̑h̵̯͐ė̵͇ ̴̰̊i̷̫̒c̸̖̀o̵̔ͅȑ̶̮ḙ̵̑ ̵̗̑f̵͉̈ó̸̱r̵̛̘ ̵͍̓ṫ̴̝h̷͙̒e̷̞͒ṁ̸̨s̸̡͘ę̴̾ĺ̸̠v̴͙̒ḙ̶̒s̵̹̀.̴̠͒/."
    },
    {
      "name": "Text Part 4",
      "tags": "",
      "id": "31",
	  "knowledge": 10,
	  "corruption": 10,
      "text": "\"I̴̧̞͙͎͚͊̅t̵̨̺̗̊̓̏ ̵̯̦̹̄̊̈́͊̕i̸̢̛̱̦͌̆͒̑ș̵̠̩̙̇ ̶̤͓̰͐͑ỏ̶̟̭̞̀̿̂̚b̴͙͔̰̮̳́̈́͠v̸̪̱̘͓̆̎̿̄i̵̜̓ȯ̴̮̳̜̿͒ṵ̶̢̗̥̜̐͆͂̿́s̸̠̺̑̏̕ ̵̦̦̞̐̔t̶͙̩͊̀h̴̢͇̖̅̄́ä̵̢͓̼̘̪́͌t̵̤̖̉͑̈̓ ̵̢̙̝͈̂̃͜ẘ̸̼̼̞̞͂ȩ̷̮͖͖̀̌̌͘ ̴̡̼̺͈̌̌̓͆w̷̻̭͓̤̜̐͋͐͘o̸̡̲̤͈̬̿̽͗̿u̵͎̤̙̥̾̾́̚l̶̫͋̑̊̎̾d̵̨̙̭̦̰̂ ̷̛̣̰̻̞͓̆c̵̢̙̠̪͛̌̚͝ó̷̳̻̪̙̙m̸͉͎̹̭͚͌̑è̸͎̝̮̝ ̸͈̗̥͇̋̋t̸̙̓̃́̕ͅo̶̹̰̥̱͖͆͛͋̀̀ ̵̧̜̄͂̌r̶̩̩͍̲̈́͑̒̂̕ȇ̷̠̭͔̏p̷̘̲͈̤̓͝l̸͈̙̆ạ̵̧͔̿͆̋ͅc̵̡͉̼͛̅ͅe̶̼̳̖̼̭̚ ̸̳̟̓̓̔ţ̴̩͈̬̥̃̽̆h̷̛̭̻̭̳͎͗̊̌̈e̵̛̘̩̝̽͒ ̶̗̠͉̦̓̔͛h̷̯̓͗̈́ư̶̰̳̈m̵̡̥͉̽̅̈́a̴̬͠n̶̠̋͐ṣ̷̡̱͂̕.̶̦̙̅̀̌͋̏ ̷̳̘͌͗T̶̺̰̪̂͝͝h̴̼́͆̄ë̸̡̻̪͇́̅i̶̬͓͓͖̋ŗ̵̮̮̥̈͂̆ͅ ̵̤̯̻̲̰͊́̈́̔͘d̷̬͂̈́i̵̳̳̯̹͖̿̈́s̵̲͚̠͇̈́̑̄̄g̷͉̺̟̩͒u̷̠̟͉͂̄͂͌ś̵͚̙͉̹̟t̸͐̓̈ͅĭ̶̯̩̲͔̥͠͝n̴̜͇͗͒͌̕͝g̸̞̦͍͑̑̇̂̕ ̸̖̪͇̈̅ǵ̸̛̭͌̀̚e̷̛̱͉͗̍͊n̴̨̠͙͈͔͌e̴̜͚͈̔̅ş̵̰̮͓̩̃̏ ̶̟̿ẁ̸ͅe̷̘̞̩̻̅͌͝͝ͅr̸̛͓̘̗͍̃̂͘̚è̵̟̥͍ ̸̺͉̪͇͍͂̊̾̈́̾f̴̺͘à̶̼̈́͊r̸͓̜͆̂̇ ̸̛͓̔̈ͅt̷̖̱͠o̷̺͔͓̱̅̓̈́ ̸̡̯̟͙͐̾̒w̷̛̱͐̈́͝e̷̙̞͍͇͍͒̔͑̃ȁ̸̱̙͕͂͛k̵̜̜̋͐͒̕ͅ ̵̬͙̃̾t̷̡̙̺͙͔́ơ̸̢̱̗̝̯͒̂͘̚ ̷̢̭̙͐̆s̶̫͛u̴̩͚͋̈́͘p̴̼̞̳͛p̶̥̳̻̉̃̒̍ͅȏ̶̙͈̰͍̽r̶̪̉͂ṯ̸̀̏ ̴̧̧̩̐ḯ̸̡̧̹̜͖̕c̸̮̼̠̜̜̃̇̽͘h̸̥͠ȯ̸̩̝̘̩̳̂̅r̷̜͐̀̈ ̵̢̳̥̟͓͗̅̿͗i̶̝̳̥̠̣͐͊n̵̖͉̖͕̮̏͌ ̷̞͙͚̝͕̑͆̀i̵̢̬͘͜t̶̼͉̯̒͒̈́̈́s̶̛͚͑̽̔ ̵̧̞̻̗̺̃́f̶̞͈̘͚͖́̎̂̒̚u̷̬͉͔̇̚l̷͚̤̉̐͝͝ľ̶̗̯͎͉͙ ̵̼̊͗̇͒͘g̷̛̦͂͐͑͝l̷͍̻̻̏͝o̶͐͜r̸̪̫̠͍̿ͅŷ̶̦̮̳̐̔͜.̷̳̟͎̂ ̸͔͚̌̐̋͜T̶̢͖̬̦̀̈́͌h̶̩̬͍̔̉̿e̶͔͑̋͒i̷̪̿̿r̸̯̿̅̄͜ ̷̨̮͈̗̭͛͐͛f̵̞͓̥̞̉͋̏̚ĺ̴͈̩̓͝ẻ̷̡̫͙̣̔g̶̪̻̔͗̈́̐́d̴͇̰͂̃̓ĺ̶̩̥̣͙̈́̒̒͜ì̵̗͝͝n̷͈̮̱̫̈́g̷̺̏̆͜ ̷̯̜͍̹̚p̷͉̈́͂̽ṍ̴͍̱͈͇͜͝ẇ̶̼̟͔̊͒͂̑͜e̸̫͕̼͔̒͆r̴̗̒̂͛s̵̞̣͛̀̒̐͠ ̵̲͎̳̾̋̈́̑̉ẃ̷̟̩͗͂̃̃ĕ̵̠̪̣̳̯̑͗̚r̶͓̣͍̈́͆ę̷̩̘͐̊̍̏ ̵͕͎̭̅̉͛̂͝n̷̙͉͌͂͠ō̸̢̡͇͎̯̎̇̚t̴̪͈̝͛́̓h̴̨͕̱͔̑̚ị̴̾̀n̶̺͋́̕ͅg̵͙͕̱͗́̐̈́ ̸̤͍͉͋͘ḯ̸̖͂͝n̸͍̽̏͜ ̵̧͉̣̙̬͛́̓̌̄c̵͇͔̙̺̑͠ǫ̵̩̭̳͈̊̒̽͋m̵̛͚̼̣̀͝ͅp̶͉̦͚̀̈̑ạ̶̓̕r̶̜̯̬̗̿̃͗e̴̪̓͂̇͊d̷̬̱̣̺͐͊ ̴̙͊͂̅ͅț̴̡̘̟͂o̵͉̐̀̌̄̏ ̷̻̜̥̩̝̓̌̉͗̂ŏ̶̭̠̭u̵̧̼͚͔̓͆́̎͝ṟ̷͙̅͘ ̴̧̗͇̯̩̅͂̀̾g̶̦̀̂l̸͚͚̤̓͛͆̆͌o̷̡̧̳̠̚r̶̬̿̒͠ͅy̵̛̘̱̬.̴͕̰̹̱̔̏̒͛͜ ̸͚̠̀Ẃ̵̡̫̟̘̽e̸̱̯̞͐̈͛̓ ̶̧͔̑́̍ȁ̵̢̫̣͕r̶̘̲̰͒̂͗̋e̵̳̥͈̜͆̇͜ ̶͕̠͚̘̥̄̉̈́t̴̖͈̜̟̒́̀̓͠h̴̙̳̰͛̓̚͠e̸̜̲͈̰͖͒͛̿ ̷̤͉͊̈́̊t̸̩͕̀̌͗͑̚r̸̟̻̩̒̔̈́͒u̷͕͌̿͝e̸̞̒͠ͅ ̵̺͒̽̏́c̴̡̱̃h̴̛̤͐̅͐̚i̸̗̾l̵̬̩͚̎̂d̴̼̲̮̕͜r̷͎̓̑̒̄͝e̴̛̩̹̭͕̯͝n̶̠͓̓͋̚ ̸̨͔̍̽͛͗ȏ̴̧̮̰̬͚̈̈f̶̮͍̏̿̇ \tT̷̛̙̅̆̊̈́̆̓̓̉̈́̂͆̀̋̓̐͗͜͠͝ͅḩ̸̛̝̽̽̾̑̽̍̎̐̃̅̇ę̵͍͚̝̱̘͖̠̥͖̼̰̣̞̟̯̈́̒̑̄͒͂͘͘ͅ ̶̳̰̏͆̄́̃̍̽̓͆́͐̆̕͘͝G̶̨̡̤͇͈̺̠̘̙͎͎̯̙͖̰͙̯̿̈́͋̋̉͐͗͛͐̽̐̈́̚͘r̴͚̠͕͉̗̗̫̥̩̎̈́̿̓̀̎͂̍̽e̵̡̧̝̞̘̪̗͔̯̝͉̅͑ͅͅā̵̧͇̮̩̰͓̱̺͓̤͔̖́̿͊͊̇̆̋͐͊̍̈́̀̚͝͠ͅt̷̢̡͔̮̭͓̤͔̗͉̾̄̀̌̊͗ ̸̟̻̹̤̹̟͍̭͓̙̖̣͛͊̒̊̍̑͝ͅǑ̸̫̻̗̖̹̪̣̳̾̏́̂͑͘͝l̶͖̳͔̻̬͈̰͊͊͊͛̀͋͌̽̏̿̄̒̏̆̈͐̚͝ḋ̴̢̞͎̜͉̙̙̠̫̺̫͂͌̂͋̾̅́̅́̂͋̎̓̉̀͠ ̵̨͎̙̮͓̫̦͉̫̩̋͂̅͒̿̈́̈́́Ờ̴̢̨̡̰̫̞̞̟̥̂̓̄͒̽̕͜n̶̨̧̬̟̘̖̭̬͍͇̝̥̬̯̳̈̎̍͋͒̆͊̏̇͠͝e̴̢̡̛͈̲̭͚͇̾̉̑̈͌̆͑̈́͊̿̑̕͝͝͝s̶̨̩͈͇̲͎̱̞̭̥̖̟̥͔̳̯̗͛̊̃̕͘͝\".\"\n\n\n[[CONTINUE|Text Part 5]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "Text Part 5",
          "original": "[[CONTINUE|Text Part 5]]"
        }
      ],
      "hooks": [],
      "cleanText": "\"I̴̧̞͙͎͚͊̅t̵̨̺̗̊̓̏ ̵̯̦̹̄̊̈́͊̕i̸̢̛̱̦͌̆͒̑ș̵̠̩̙̇ ̶̤͓̰͐͑ỏ̶̟̭̞̀̿̂̚b̴͙͔̰̮̳́̈́͠v̸̪̱̘͓̆̎̿̄i̵̜̓ȯ̴̮̳̜̿͒ṵ̶̢̗̥̜̐͆͂̿́s̸̠̺̑̏̕ ̵̦̦̞̐̔t̶͙̩͊̀h̴̢͇̖̅̄́ä̵̢͓̼̘̪́͌t̵̤̖̉͑̈̓ ̵̢̙̝͈̂̃͜ẘ̸̼̼̞̞͂ȩ̷̮͖͖̀̌̌͘ ̴̡̼̺͈̌̌̓͆w̷̻̭͓̤̜̐͋͐͘o̸̡̲̤͈̬̿̽͗̿u̵͎̤̙̥̾̾́̚l̶̫͋̑̊̎̾d̵̨̙̭̦̰̂ ̷̛̣̰̻̞͓̆c̵̢̙̠̪͛̌̚͝ó̷̳̻̪̙̙m̸͉͎̹̭͚͌̑è̸͎̝̮̝ ̸͈̗̥͇̋̋t̸̙̓̃́̕ͅo̶̹̰̥̱͖͆͛͋̀̀ ̵̧̜̄͂̌r̶̩̩͍̲̈́͑̒̂̕ȇ̷̠̭͔̏p̷̘̲͈̤̓͝l̸͈̙̆ạ̵̧͔̿͆̋ͅc̵̡͉̼͛̅ͅe̶̼̳̖̼̭̚ ̸̳̟̓̓̔ţ̴̩͈̬̥̃̽̆h̷̛̭̻̭̳͎͗̊̌̈e̵̛̘̩̝̽͒ ̶̗̠͉̦̓̔͛h̷̯̓͗̈́ư̶̰̳̈m̵̡̥͉̽̅̈́a̴̬͠n̶̠̋͐ṣ̷̡̱͂̕.̶̦̙̅̀̌͋̏ ̷̳̘͌͗T̶̺̰̪̂͝͝h̴̼́͆̄ë̸̡̻̪͇́̅i̶̬͓͓͖̋ŗ̵̮̮̥̈͂̆ͅ ̵̤̯̻̲̰͊́̈́̔͘d̷̬͂̈́i̵̳̳̯̹͖̿̈́s̵̲͚̠͇̈́̑̄̄g̷͉̺̟̩͒u̷̠̟͉͂̄͂͌ś̵͚̙͉̹̟t̸͐̓̈ͅĭ̶̯̩̲͔̥͠͝n̴̜͇͗͒͌̕͝g̸̞̦͍͑̑̇̂̕ ̸̖̪͇̈̅ǵ̸̛̭͌̀̚e̷̛̱͉͗̍͊n̴̨̠͙͈͔͌e̴̜͚͈̔̅ş̵̰̮͓̩̃̏ ̶̟̿ẁ̸ͅe̷̘̞̩̻̅͌͝͝ͅr̸̛͓̘̗͍̃̂͘̚è̵̟̥͍ ̸̺͉̪͇͍͂̊̾̈́̾f̴̺͘à̶̼̈́͊r̸͓̜͆̂̇ ̸̛͓̔̈ͅt̷̖̱͠o̷̺͔͓̱̅̓̈́ ̸̡̯̟͙͐̾̒w̷̛̱͐̈́͝e̷̙̞͍͇͍͒̔͑̃ȁ̸̱̙͕͂͛k̵̜̜̋͐͒̕ͅ ̵̬͙̃̾t̷̡̙̺͙͔́ơ̸̢̱̗̝̯͒̂͘̚ ̷̢̭̙͐̆s̶̫͛u̴̩͚͋̈́͘p̴̼̞̳͛p̶̥̳̻̉̃̒̍ͅȏ̶̙͈̰͍̽r̶̪̉͂ṯ̸̀̏ ̴̧̧̩̐ḯ̸̡̧̹̜͖̕c̸̮̼̠̜̜̃̇̽͘h̸̥͠ȯ̸̩̝̘̩̳̂̅r̷̜͐̀̈ ̵̢̳̥̟͓͗̅̿͗i̶̝̳̥̠̣͐͊n̵̖͉̖͕̮̏͌ ̷̞͙͚̝͕̑͆̀i̵̢̬͘͜t̶̼͉̯̒͒̈́̈́s̶̛͚͑̽̔ ̵̧̞̻̗̺̃́f̶̞͈̘͚͖́̎̂̒̚u̷̬͉͔̇̚l̷͚̤̉̐͝͝ľ̶̗̯͎͉͙ ̵̼̊͗̇͒͘g̷̛̦͂͐͑͝l̷͍̻̻̏͝o̶͐͜r̸̪̫̠͍̿ͅŷ̶̦̮̳̐̔͜.̷̳̟͎̂ ̸͔͚̌̐̋͜T̶̢͖̬̦̀̈́͌h̶̩̬͍̔̉̿e̶͔͑̋͒i̷̪̿̿r̸̯̿̅̄͜ ̷̨̮͈̗̭͛͐͛f̵̞͓̥̞̉͋̏̚ĺ̴͈̩̓͝ẻ̷̡̫͙̣̔g̶̪̻̔͗̈́̐́d̴͇̰͂̃̓ĺ̶̩̥̣͙̈́̒̒͜ì̵̗͝͝n̷͈̮̱̫̈́g̷̺̏̆͜ ̷̯̜͍̹̚p̷͉̈́͂̽ṍ̴͍̱͈͇͜͝ẇ̶̼̟͔̊͒͂̑͜e̸̫͕̼͔̒͆r̴̗̒̂͛s̵̞̣͛̀̒̐͠ ̵̲͎̳̾̋̈́̑̉ẃ̷̟̩͗͂̃̃ĕ̵̠̪̣̳̯̑͗̚r̶͓̣͍̈́͆ę̷̩̘͐̊̍̏ ̵͕͎̭̅̉͛̂͝n̷̙͉͌͂͠ō̸̢̡͇͎̯̎̇̚t̴̪͈̝͛́̓h̴̨͕̱͔̑̚ị̴̾̀n̶̺͋́̕ͅg̵͙͕̱͗́̐̈́ ̸̤͍͉͋͘ḯ̸̖͂͝n̸͍̽̏͜ ̵̧͉̣̙̬͛́̓̌̄c̵͇͔̙̺̑͠ǫ̵̩̭̳͈̊̒̽͋m̵̛͚̼̣̀͝ͅp̶͉̦͚̀̈̑ạ̶̓̕r̶̜̯̬̗̿̃͗e̴̪̓͂̇͊d̷̬̱̣̺͐͊ ̴̙͊͂̅ͅț̴̡̘̟͂o̵͉̐̀̌̄̏ ̷̻̜̥̩̝̓̌̉͗̂ŏ̶̭̠̭u̵̧̼͚͔̓͆́̎͝ṟ̷͙̅͘ ̴̧̗͇̯̩̅͂̀̾g̶̦̀̂l̸͚͚̤̓͛͆̆͌o̷̡̧̳̠̚r̶̬̿̒͠ͅy̵̛̘̱̬.̴͕̰̹̱̔̏̒͛͜ ̸͚̠̀Ẃ̵̡̫̟̘̽e̸̱̯̞͐̈͛̓ ̶̧͔̑́̍ȁ̵̢̫̣͕r̶̘̲̰͒̂͗̋e̵̳̥͈̜͆̇͜ ̶͕̠͚̘̥̄̉̈́t̴̖͈̜̟̒́̀̓͠h̴̙̳̰͛̓̚͠e̸̜̲͈̰͖͒͛̿ ̷̤͉͊̈́̊t̸̩͕̀̌͗͑̚r̸̟̻̩̒̔̈́͒u̷͕͌̿͝e̸̞̒͠ͅ ̵̺͒̽̏́c̴̡̱̃h̴̛̤͐̅͐̚i̸̗̾l̵̬̩͚̎̂d̴̼̲̮̕͜r̷͎̓̑̒̄͝e̴̛̩̹̭͕̯͝n̶̠͓̓͋̚ ̸̨͔̍̽͛͗ȏ̴̧̮̰̬͚̈̈f̶̮͍̏̿̇ \tT̷̛̙̅̆̊̈́̆̓̓̉̈́̂͆̀̋̓̐͗͜͠͝ͅḩ̸̛̝̽̽̾̑̽̍̎̐̃̅̇ę̵͍͚̝̱̘͖̠̥͖̼̰̣̞̟̯̈́̒̑̄͒͂͘͘ͅ ̶̳̰̏͆̄́̃̍̽̓͆́͐̆̕͘͝G̶̨̡̤͇͈̺̠̘̙͎͎̯̙͖̰͙̯̿̈́͋̋̉͐͗͛͐̽̐̈́̚͘r̴͚̠͕͉̗̗̫̥̩̎̈́̿̓̀̎͂̍̽e̵̡̧̝̞̘̪̗͔̯̝͉̅͑ͅͅā̵̧͇̮̩̰͓̱̺͓̤͔̖́̿͊͊̇̆̋͐͊̍̈́̀̚͝͠ͅt̷̢̡͔̮̭͓̤͔̗͉̾̄̀̌̊͗ ̸̟̻̹̤̹̟͍̭͓̙̖̣͛͊̒̊̍̑͝ͅǑ̸̫̻̗̖̹̪̣̳̾̏́̂͑͘͝l̶͖̳͔̻̬͈̰͊͊͊͛̀͋͌̽̏̿̄̒̏̆̈͐̚͝ḋ̴̢̞͎̜͉̙̙̠̫̺̫͂͌̂͋̾̅́̅́̂͋̎̓̉̀͠ ̵̨͎̙̮͓̫̦͉̫̩̋͂̅͒̿̈́̈́́Ờ̴̢̨̡̰̫̞̞̟̥̂̓̄͒̽̕͜n̶̨̧̬̟̘̖̭̬͍͇̝̥̬̯̳̈̎̍͋͒̆͊̏̇͠͝e̴̢̡̛͈̲̭͚͇̾̉̑̈͌̆͑̈́͊̿̑̕͝͝͝s̶̨̩͈͇̲͎̱̞̭̥̖̟̥͔̳̯̗͛̊̃̕͘͝\".\""
    },
    {
      "name": "Text Part 5",
      "tags": "",
      "id": "32",
	  "knowledge": 10,
	  "corruption": 10,
      "text": "\"̸̡͈̦̳̫̃̒̌̎̿͘T̸̨̨̛̛̙̮̼͈̦̺̗̀͐̄̑͗̎̏͌̓͌̑͑̑̕͝͠h̷̜̤̥̦͓̳͇̣̹̮̻͉̣̼͇͋̂̌̽̄̑̄̋̇͑̽̊͊̊́͘͝e̶̡̡̧̧̫̭̥̣̫̫̪̣͎̳̭͉̻͖̮͕̼̖̝̅̔̽̾̒̅͐͋͋̎̕͝͠n̴̛̰̱̳̰͇̳̫̥̮̹̪̎̏͛̃̾̊̈́͑̔̄̾̏̕̕̕̚̕͝ ̶̧̞̮͍̝͈̱͈͓̀̃̊̓̊̔͘͝͠͝͝ͅt̷̜̺͎̗͊̾̈́̽̾͒̽̃̆͋̃̅͋̀̚͜͝ͅȟ̷̛̞͉͎̥͍̥̩̘̜͆̉͑͜ͅę̴̢̦͎͓̗̞͉̞̙̟͕̱̟͙̠̙́̉̋̅̓̂̓̈́̅͛̃̑̈́̽̔̍̊͋̽͝ ̸̧̧̨̹͉̰̙̞̰̞͙̩͙͎̯̮̘̓͆̽̾͊͗̓̽̿̇̽̓͒͋̌́͐̇͋̇͘͘̕͝c̸̲̋͋̈́̈́̔̄̂̓̓͊͌͒ͅr̵̨̨̨̢̢͙̹̝̝̳͔͈̲̗͉̪͚̙̩̫̯̪̞͂̏́͗̓͗̋̆ę̷̲̙̖͇͚͉̹̼͈͈̟͇̭̬̼̰̝͖̩̉̈́͆̑̎̒̎̏̌̈̅̄͒̎̿͘̕̚͝ͅͅa̵̧̨̧̛̼̟̤̜̗͚̜͈̭͖̲͖̳͇̓̏̊̆͌̏̇̎̈́̆́̓̈͐͋̈́́̒͜͠t̷̛̟̱̪̠͇̲̞͓̤͖̱̭̫̒̎̓͛͋̿̈́͛̌̓̇̉͑̒͛̇̾̎̉͆͘͘͜ò̸̢̧̓͐̽̇́͋̿͆̎̕̕r̶̨̹̹̲͓̭̉̓̉̂̆̀̽͐̈́̅̉̆́̆̊͋̒͐̂͋͘͝s̵̨̖̪͚̬̜͇̻̞͓̪̬̜̘̬̲̦̉͜͜ͅͅ ̵̛̜͔̻̻͕̼̙̺͚̰̰͍̹̂̆̓̏̌͋͗̐ở̸̛̘̜͇͒͒̈́́̌̆̊̋̑͆̚f̷̯̼̮̦͈̹͖͍̦̑́́̂̌̐̆̀̿̑͒͐̓̔͊̄́̈̎̏̔̈͑̕͠ ̴̡̧̼̭̣̫͉̣̹͙̟̟͖̼͙͉̮̯̖̻̠͕̭͇͒͊͛͑́͛̊̿̋̈́̒͛͐̀̓͗͐̓͆͘͠͝T̸̲̯̆͂h̷̡̢̡̡̛̘͇̹͙̰̰͍̳̟̮̝̪͉͕̯͈͍̘̯̠̔̍̀̃͑̀̄̃͊͑̒͂͠e̷̢̢̙̫̹͙̹̱̟̖̯͚̖͉̞͍͈̼̜͙̪̥̜͂̆͆̀͆̀͐̏̓̔̀̐͂̕̕̚͠͝͝ͅ ̸̧͍͓̟̻̣̻͉̥͖̪̟̓͜͠Ơ̵̧̥̯̝̱̯̻̞̺̘̜̓̓̅̽̂̇̀̅͛͛̈́̑͑͌̀̚͜͝͠l̵̨̧̨̢̛͎̯͒͛͌̾͋̄̈́̍͐̔̐̔͘͝͠d̷̨͔̙̯̦͇̲̝̻̾̒̀̑̏̌̓́͝ ̶̨̛̥̼͇̭̙̯̀̀̆̅͗̂͝Ỏ̵̧͎̺̜̱̪̱̈͂n̶̨̡̯̤̟̭͔̰̰̜͍̘̺͉͈̝̰̮̝̻̜̯̬͂͗̔̈̎͂͒̈́͌̌͝e̶̳̣͓͉̹̤̘̰͇̲̯̳̙͎̞͚̊̓̈́̈́̏͗͋͜ ̶̹̩̺̹͚̫̦̣̯̲͎̼̭̯͚̰̭̹͕͎̙͖̭̂̅̌̅͐̉̎̂̽̑͒͜͜͝͝ẅ̴̨̢̜̻̣͓̪͙̝̳̪̱͈̟̺̯͕̦̖̹̑̑̉̀̉͆̊͗̓o̶͕̪̝̻͓̦̝̓͑u̴͚̒̅̃̌̈́͛̂̀̅͗̈́́͌͆̚͝͠ͅl̴͍̳̱̭̣̥̣̰̺̝̳̍̔̀̾͒̾̒͜͝d̶͙̮̪̦̰̯͆͑̋͋̑́̆̀͆̐̄͘͝ ̷̧̡̡̛͍̦̮̪͉̥̠̙͓̣͉̤̭̖͔͆͋̓̿̾͋͊͂͛͗̊̈́͘͘͝t̴̢̨̢͖̗̤̹͓̦̪̭̳͈͉̖̗̩̯̘̞͓̄̅̋̂̀̀̆̽͋̎̀͌͒̾̎̍̕͜͠ͅͅḩ̶̦͚̺̱̪̊͑̐͊̓̈̈́̀͋̎̍̓̀͋̒̕͜͜ͅé̴͔̥͙̣͍̞̝̹̺̥̫̬͌̈́͐ń̷̨̨̛͔̏̐̓̓͗͂̒̓̚͘͝͝ ̴̢̨̦͖͚̥̼͈̺̤̗͖͕̰̙̜͙͕̣̱̬̓̈́͑̏̌̕͘͜͜͝ḏ̵̛̻̙̒̌̽̓̐̎̽̈́̾͂̏̑̓̚͝e̷̡̞͓͙̞͔̯͓̖̳̝̞̦̹͔͈̿s̸̖̼͝ȩ̷̨̢̘̠̝͕͚̌̿̌̐̂͆̽͑̒͌͘͠n̵̨̧͉̖̦̫̮͇̜̞̳̬͚̘̲͓̏ͅď̶̨̧̛̮͕̤̘̯̩̯͔̖̺̠̜͕̟̩̣̬͈͖̣̎̈̾̈́̇͐̍̄̌̚ ̷̛̠̲̣̎̌͛̈́͗̀̓͛͆͂͒̍͋̏́͒͘̕͝͝f̴̧̗̺̙͈͇̠̙̠̉̈́͑̊̏͋̈͒͛̇̽́̋̍͝ͅr̷̨̳̪̪̖͖̹̹̻͉̔̈̿́͛̍̈́̐̌̒̈͑͂̿́́̉́̚̚͘͝͠o̸͖͈̞͚̼̬̤̼̹̦͆͋͒̑͐̐̃̋́̒̅̑͠m̶̧̡͚̖̼̻̣̰̦̝͈̦̤̺͉̗̠̩͎̌͂̍̓̀̓̍͗͌̓͒̿̓͋̒̃͌̃̑́̚͘̕͝ ̸̢̟̯̩̭͙͈̣̮̬̞͕̘̗̟̤͈̠̮̣̫̟̩̌̓̓̒̈́͒̊͐̔̚t̶̟̪͎͕͉͋̈́̎̎̄̀̃̌̊͌͊̄̃̋̊̈́̆͠ͅh̶̛̛̹̐̌̌̈̂̎͛͑̈̒͊̓̍̈̀͛̒̀̊̍̕͝͠è̸̹͓̤͎̌̈́̾́̈́̐̅ͅ ̸̡̡̨̨̖͔̩̱̠̥̺̩̦̝̩̺͙̩̣̙͔̉͂̓̌͂͊͂̌̀͐́̓͘͝s̴̡̹͍̦͈̮̗̬̞͓̐̿̿̈́k̵̗͕̺̟̯͓͗̾́̐͂̈́͊̅̆̋̋͐̊̈́̓͆͊̕͘̕̚̕͠ͅy̸̯͉͉̬̗̣̿̿̇̆̋̒̍̐̉͒͋̉͆̋̽̔͂͒̽̿͊̓́̐͜͝ͅͅs̶̛͖͎̹̯̓̈́̔͗̈,̵̡̡̢̨̧̲̮̩͖̼͈͈͓̹̺̭̞̟̞̩̳̥̖̈́̇̒̐̅̎̀͑̓̔̕̚͘͘͘͜͜͝͝͝ ̴̜͉̳͉͉̫̣̮͛̔̌́̀̓̾̀̋͗͋̍̾͆̑̏̌̓̎̐͘̚̚͠͝ţ̸̧̨̮̩̮̜̹̳͓̌̂̓̍́̈́̕͜h̶̡̦̝̺̠̳̻̎̓̌̕e̴̛̲͍̪͛̅̽̀̓ý̸̧̻̠͎̝̤͓̝̖̘̤͔̰͖͒̀̎͌͆͛͐̓͂̎͗́̾͒͌̅̾̽̀̈́̚̕͜ ̸͉͕͙̜͕͍̘̦̗̖̻͖͓̘͕͇̲̻̳̟̮͋͆̏̈́͐̊̌̓͑̃̈̐̇͂́̽̈́̃́̚͘w̴̨̺̙͓̤̠͎̖͊̀̊̄̄̒̎̃̍o̶̰͇̟̣͎̜͓̗̭͛͐̋̐͐̐̊̎̉ư̷͔̝̜͉̹̗͖̞̺͇͖̗̲͙̑͗̌̀͂̉̎́̌̑́̃͛͊́̓̍̆̌̕̚̕͝͠ͅḻ̷̛̼̘̱͉͕̭͉̙͈͙͉̬̪͇̩̭̠̥͖̻͍͊̈͒̀̅̌̾̓ͅͅd̶̨̛̞̜̙̼̳̦̳̱͍͍̪̯͌̔͊̊̾̄͑̀̈́̈́̈͒̊͒̓́̌͂̈́͒̆̕͜ͅ ̸̢̼͕̰̱͉̰̹̬̙̭̳͙͖̋͛̓̌ͅͅc̶̢͍̞̼͉̮̜̺̗̝͚̲̳̤̪̼̒͌̂̈́͆͂͒́͊͊̈́̓̋̚ô̶̙̤͍͔͖͍͚̥̝̖̞̠͊̅̏̉̇͂́͛̌́̂̈̿́̾͑͘̕̕͠͝͝͠m̶̨̡̧̛̙̞͉͇̲̩̙͉̯̝̖̹̖̯̖̘̲̼̘̪̋̉̈̓̀̓̌̅̈́̑̊́̒̓̓͛͐̒̓̌͑͘͜e̸̡̧̢͍̪̥̙͇̬͌̅͑̾̑̓̀̿͐̈́̏͝ ̸̡̛̞̘̲̘̳̪̳̘͍̻̼̣̥̟̔̑̎͊̇̄͆̃͝ͅͅt̶̢̛͕̙͉̝̹͕͖͎̲͗̌̀̈̏̌͒̀͐͂͗̈́̂̕͘͠ö̸̢̨͍̫͕͙̫̳̮̖̫̝͎̭͎͈̣̖͓̻̞̩̜̦̳́̏͒͗͗̊͌̑̓̀̀̈́̆̍̾͆͌͐̇̈̀ ̸̦̅̇̇̏͒̈́̈̊̀͂̆͑̒̍̇̀͛̅̅͋̉̇b̸̧̝͓͎͖͔̦̻̯̱̪̟̾͂͆͒̈̊̏͑̀̇̑̓̋̑̓͌̋̀̚̕͘l̸̰̺͓̇͌̅̃͒̈̏̅̐̀̒̏̂̐͂̕̚̚̚͝͝ě̸̺̪̥̮̣̤͕͔̹̫͚̞̓̋͋̽͂̏̄̆̓̈́͝s̷̨̨͍͖̪͓̞̙̱̣̻̙̰̮͒͜͠s̵̨͚̪̜̤͙̯̫͍͎̥̻̙̪͚̖̀̐̊͠ ̸̡̡͔̝̥̩̤̟̥͈͇͇͆̈́͌h̶̢̛̗͕͇͍͓͎̩̻͖̘̘͎̰̟̅̐̈́̾̄̏͐̓̎̓͆̽̎̑̚ų̵̨̝̟̰̤̞̞͕̺̼̺̼̹̯̩̝͍͎̦̝̄̔̋̊͌̽̑͂̒̿̅̄̃͘͜͜͜͝ṁ̶͈͈͈̗̅̾͆͊̉̕a̷̪̯͓̙̣̥̪̥̺͍̞̲̯̙͈̮̘̝̅́̎͂̃̀̓̅͑̓̑͒̅̉́̎́͊̍̕͜͝͠͝͝͝ͅň̶̦͍͎͌̈́̊i̸̡̠̣͍̗̩͈̪̭̬̖̘̹̥̮̐́ͅͅt̵̡̧̮̲̯̠̳̩̟̦̺͈͈̩̠̻͎̳̻̱̫̖̩̜͛͗͊̄̽̎̂͋͂̕͝͝y̸̢̛͖̯̗̗͕̘͍͚̟͚̞͈̮̥̝̳̘̫͉͐́͊͌̀̎̓̎̓̆͂̂̀͆̓̄͌͋͐͘̚̚͝.̵̨̧̛͉̻͎̩̪̯̙̞̽̋̏͂̂͌̂̚͜͜͝ͅ ̵̧̛͖͔̹̤̜̝̝͂̈́̓͋̎̓̂͂͘B̶̥̟̥͙́͠ȕ̵̡̞͈̣͔̤̘̤̯̣̬̟̬͇̳̙͋͛̏̈͝t̷̛̠̖̬̘̞̜͔̳́͑̆͆̇͂̈́̌̕͝͝͝͝,̴̨͈̫̮̦̤̩̞̟͖̜͇͍̦̳̘͓͚̮̓̀̊̒̿̔̕͠ ̷̡̛̰̮̥̗̠̫̩̥̯̩̲̺͇̩̜͚̩̹̹̝̄̈̅̒͛̎̓̿͊̊͑̕t̵̢̧͚̬̳̫̞̮̗̮̏̋͒͌̀̿͒̓̇͐̆͑̒̈̊̂͐͆͊͐̇̉̚͝h̴̻͍͖̟̹̪͑̚ȩ̸̛̞̤̩̞̝̼́̽̐͆̂̾̍͜͠͠ ̶̫̼͉̘̤̞̗̙͙̩̟̙̳̄͒͗̄̌̈̔̐̔͊͗͗̏̓̑́͘d̸̨̧̧͉̜̥̬͉̮̰̠̠͍̳̟̩̱̩͍͕͇͇͓̍̔̀̈́̅͑̂̈́̆̇͋́̎̾͛͒̐͊̚͠͠͠ę̵̡͙̪̬͓̬̤̙̙̯͚́́̎̒̆́͂͗̄̽́̕͠ş̶̢̞̻̳̼͚̞̞͚̼̤̋̀̔̈́̄̓͠ģ̷̡̟̞̮̜̤̞̖̹̞̘̖͍͖̳̘̪̜̤͑͗̏̉̍̆̋͑͒̀̈́̇̂̐̅̾̾̿̚͝u̷̡̦͕̫̱͚͓͕̜͎͉̫̲̞̦̭̲̇̌͆͠ş̷̨̫͉̳̹̜̣̰̜̺̣̺̘̫̻̓̎̃̏́̉͑͐̈́̕͜ț̴̡̛̦͍̫̣̜͙̘̮̠͙̭̘̦̪͖̖̰̭̬̲̥̿̑̉̆̈́͂̓̏͑̔͛̀̍̾̾̏͆̉̕̚̚̕͝͝i̷̢͓̮͙͈̱̫̞̩͒͆̈͒̈́̾̑͒̄̿͗̐̏̋̈́̇̾̕͘ņ̶̢̝̹͔̳̜̲̳̬̪̿̒̐̈́̾̾̓̅̓̈́̍̿̃̾͠g̵̢͇̘͚̱͈͇̦͐̂̒́̄̓̑̅͘ͅ ̶̢̛̦͙̠͚͕͙͈̤́̃͂̓̿̃̈́̄͐̈́c̸̢̨͎͙̣͖̺̰̗̖͈̙̩͚͍͙̭̰̾̈́͑͊͑̒͝r̶̢̧̢̛̗͍̺͙͉̯͇̖̯̙̣͇̻̫͕͚̗͇̘̈́̆̌͋̇̈̋͛̄͛̓̆̈́̆̿̾̈͗̕͝ȩ̴͎̲̖̦̹̪̱̙̀̒̊̾̌̓ť̴̪̥̣̗̦̹̟̪̭̹̮̰͙̹͓̞͖̩̃̀̉̏̍̓͌̾͝ͅo̷̼̝̣͓̱̤̾̒͒̌͆͆̈͛̔̒͘͘͜͝ń̵̡̧̟̮͕̼̜̼̼̟͍̳̃͋́͐͑̄̑s̵̞̲̠̘̞͈̯̜͐̑̃̽̽̓̂̆̃̂̕͠͝ ̸̨͙͚̳͍̰͒́̋̾̅̓̈́̓̽̈́̑́́̽̕͠͝ǫ̶̙̯̘͖͕͖̟̙͍̻̖͉̫̳͕̬͚̩͗̾̃́́̔̽̿̽̆͗̍͐̀̓̋̕͜͝͝ͅf̷̛̛̼͕̜͇̰̬̦͉̫̖̠̳̙̪͕̜̲̖̫̤͍͉̓́̓̓̿͒̾̿̂̇̂̀͋̀͋̽͘̕͝͝ ̷͈̺̦̠̦͈́͛̓̂̐̄̎̉̏͛͆́͑͋́ţ̸͉̼̙̰͉̖̼̰̖̔̐̋̉̓̓̈́̍́͂̈́ḧ̸̨̠͇̠̱͓̥̖̝̭͕̤̝̟̰͚̤͈̗͚̔͛̋̊́̿̊̔͊͝ͅé̴͇̥̞̫̠̥̹͍͆̂͐̆͛͊̂̄̀͗̈́͊͊̂̂͒̋̚͝͝ ̸̧̦̻̺̳̟̙͖͕͉̗̮̣͗̔͐̒͒̈́͋̔̇̍̉͋͘̚͝e̷̬̎ą̷̢̱͎͎̱̱͚͈͇̻̲̼̦̠̬͇̗̼̻͇̼̣̙͋̿͌̀̽̽ͅr̴̜̤̮̝͔͕͙̗̮̥͔̜̳̖̳̬̥̣̞̋́͐́͗͒́͌̆̆̉́̐̒͑͐̒̾͝ͅͅt̷̩͙͈̭̟̠̫͑̂̐̈́̊̂̊̾̅͂̉̇̄͗̀͆̀̒͘͝ḧ̸̡̪̳̱͈̬̺̖̬͖̠̺̦̝̈́̄͗̅͌̾̐͌͊͘ ̶̢̛̮̣̾̓͗͐̀͗̆̊̾̆̎͗̈̒̚͘͝ͅw̶͙̼̞̃̽̊͋́́͆͒̓̊̅̀̓̏̓̅̓̕͠͝͠ǫ̷͚͚͇̫̣̘͉̞̠͖̦̟͔̲̣͇̟́̉̈́̂ͅú̷̢͓̳͚͚̱̥̻͈̣̖̣̱̲̗̱̖̙͐̎̉̿̉͊̇̾̋̏̎̍͒̋̏̈̇̓͘̚͜l̶̢̦̯̳̮̫̞̰͙͖̥̠̤̺̙̻̘̥̖̩͐̈͂̒̈́̋͜͜d̶̛̟̺̦̖̗̲͍̒͛̎̏̒͐͌͂̀́̅̀̿̀̂ ̸̱̗͖̼͙͈̭̖̬̩̥͕̟̱̻̈́̽͂͐́̍̔͗͐̐̑͋͑̈́͐̈́͠͝r̴̨̛̘̖̪̳̀́̃͌͒̒̉̃̀̿͌̒̊̽̍͘͝͝e̴̢̡̧̪̘̙̱̙̺͉̔̔̔͐̔̀̕͝͝f̶̨̡̮̠̻̰̠͍̘̪̱͔̰̗̯̯̖̤͖̯͑̊̎̈́̋̂͠ų̸̧̧̙̯̺̫̩̰̣̖͚̰̙̥͙̈́̔̈͐̂̈́̈̽̕͝͝s̸̲̖̦̿̓̅͑̾́͌̔̑̅̔̋̂̽̾̿̋͂̚̚͘̚͝͝ę̸̛͚̭̖̰̲͓̲͓̻̪̭̹̯͎̫̇́͛̆̂̿͌͆͗̈́͆̋̽͊̄̋̈́̓̓̽̕̚̕͝ͅ ̶̧̢̛̻̥͔̫̻̗̣͔͎͚̼̗͖̱͉̫͓̩͗̉̔͑͊̍͜t̸͉͇͛̂̐͊̽̆̀͆͗͆h̶̗̖̝̠̥͕̃̒̈́͐̏̕ẽ̵̢̲̘͖̟̫̬̥̫͚͈̦͎̺͓͕̖̫͖͎̉̔̐̈́͂̆ͅͅͅḿ̸̢͈̟̞͇͔͓̱̳̂͂͂͊̓͑͒̇̐̏̉͒͑̍͛̽͘͝͝͠.̵̡̓͋ ̸̢̨̳̹͔̯̲̲̖̟̱̲̩͎̖̏̍̄̈́̈́̈́̍́̊͂̚͘A̶̧̘̩͗̑͛̇́͐̄̋̆̑͐̾́͗̄̐̽͊͘͘s̴̨̥̫͈̰̩̺͍̟̜͈͙͒͌͂̐͂̂͂͊̇̇͜͝͝͠ȟ̷̨͔̯͉̟̐̉͊̆̄̏́̓̚̕ͅã̵͈̼̻̘͙͙̻̈́̉̾̎̋̈́̾̎͑͐̾̒̈͆̏́̑̿̀̕͘͘͜͝͝m̴̘̤̣͔̣̯̰͇̤̠̠̹͎͚̏̈̊̽̆̌̾̈́͐͘̕͜e̷̢͖̟̼̭̭̺̯̐̈́̔͘͜͜ ̴̧̛̯͚̣̤͚̻̟̻͙̬͎̝̖̳͕̠̰͐͋͆̽̎͐͂͒̃͂́̀̉͋̕̚͜͜ͅt̴̡̧̠̖̰̣̹͓͎͈̱̥̲͒̍̽̈́́̈́͆͆h̶̢̧̻̠̘̤̝̠͔̭͖̭̦͉͉̭̹̩͖̗͍̦͈͉́̎̌͌͒͆͗̍̕͜e̸̢̫̹͉̜̅̐͆̑̃͐̈͆̀̿̀̔͊̄̋̚͝͠ͅs̴̡̛͕͉̍͂̆̎͐̊̏̿͛̈͋̋͗̆̈͋̇̋͘̕͜͠e̵̡̅͑̾́̈́͘ ̸̢̡̺̥̥̤̦̰̼̘̗̰̠͖̳̥͕̹̭͗̅̈́ͅḑ̴̢̛͚̘̞̭͇̰̖̫̮͓͉̻̜̼̘̗̪͇̰͕̖̇̀̐͂̒́͒̽̽̓̓̽̾̈͛͠i̶͔͉̫̘͖̱̗̓͛̉͋͠v̸̢̡͚͕͚͍̦̟̭̰̓̏͆̓̐͝͝í̶̧͉̯͍̫̻͉͉̬͍̖̫̼͙͇̖̫͚̰̽̃̂̕n̷̘̳̖͓͇͚͖̬͙̗̥̬̹̩̘̠̩͎̥̘̱͉͉͛̐̔̎͆̒̍̇́̽̊̍̈͌̕̕͝͝ë̶̙̹̖̳̱̹̮̗͖͇́̓̊̀̍̅̋̈́̈́̚̚͝͠ ̶̧̨̨̢̢̡̨̛̘̩͎̘̱̪̪̼͍͍̻̭̔̅́̽̉̃̆ͅb̴̪̹̲̈́͐̔̈́̆̀̈́̄̈́̇̏̾ę̸̧̡͚̱̗͍̪̘̼͚̟̯̞̪̩͈̹̦̘̥͛̈́̽͛̆̕ḯ̷̛̥̻̼̖̺̙̉͗͆͌͐̓̈̿͒͑̂̅͋̂̌̆̍̈́̚͜͠ṉ̷̡̡̹͇̖̥͍̪̟̘̫͕̙̳͎͚̳̞̻̭̆̒͊̂͆̌͛̃̒̽͆̅͊̀̄̌̕͜ǧ̵̼̰̼̻̠͕͓̲̯͉̖̣̟͇̈́̀̓̅͑̋̾̍̈́̈̾̔͠s̷̗̲̰͉̬͔̼̤̰͕̰̱͖̹̺̘͓͙̽͋͜ ̶̝͔̫̤͍͙̱̓͊͑̀͑̋̌̆̕͝ẉ̶̡̛̗̤̫̫̰̮̳̦̩̤͇̗͚͉̬̜̫͖͚͙̬̩̊̀̿͊͂̈̂̔͐͑̈́̒̆͂̋̀͗͊̎́͘̚̕͝ö̶̡̨̼̼͓͇́͋́ṳ̶̢̨̧̤̩͈̮͖̗̳̰͔̟͍̬͎̥̟̩̼̦́̈́̇̽̊̎̄͆̓̉̀̑́̆̕͘͘̕͜͝l̴͚̙̣͖̤͈̗͖̞̮͙̫̖͖̞̤̮̫̤̲̬͒͆̈́̈́͆̚͜͠ͅd̶̨̢̹̼̲͖͖̺͗̑͗̓́͐͆́̿̅ ̵̝̆̋̽̉̍̃͗́̿̅͋̓͋͠͝͝d̷̲̗̓̇̕e̷̡̧̨̞͍͙̳̞̤̺̱͓̟̤̺͈̐ͅs̴͖͈̥̗̠͓͙͍̟̥̝͔͚̲͌̌̏̑͊͘ͅt̸̙͉̦̗͙͖͈͍͎̳̞͙̱̘̏͆͊̋͂͂͑́̌̀͂̀̈́͠͠͠r̸̡̧̨̧̢̥͖̹̗̤̦̻͈̜̯̭̤͎̝͖̋̄̾͌̀̑̑̒̓͑̈͂̓̅̎͊͊͘̕̕ǫ̵̼̮̪̭͍̦͖̤̣͉̖͓̠̗̲̞̲̱̯͌ͅý̵̢̜̪̪͎͖̩͙̜͈̟̖̦̗̤̹̰̤̰̯̼̀̍̆̇͗̈́̊́̀͆͗̾̇͠͝ͅͅͅ ̷̡̛̛̱͖̩̳͖̗̼̫͈̣̺̘̥͎̪̟̬͙̟̪͍͎̋̋̋́͝ẗ̸̛̝̰͖̗̲́̀̌̑̀̽͗͒̀̌̔̋̈́̑͂̋͘̕̕͠͝͝h̸̗̞̼̗̬̗̺̯͚̻̀͐͐̀͐̍͛̾̆̊̈́̉̉͑́̓̎͝e̵̳̝͈̳̬̞̘̘̰̙̙̭̟͉̥͇̗̥̐̂̄̓͜͝ ̵̢͕̥̘̠̯̗̎̀̈́̈́̑̀h̷̨̡̡̡̛̛͎̜̙̜̮̲͔̺͚͕̩̝͒̏̅̆͐̎͑̄̋̎͝͝u̴̟̟̻͓̇͐͋̑̌͗̀̓͋̀̚̚m̴̧̢̧̮͍̘̫̬̱͕̮̲͎̬͈̬̹͙̣̮̰̟̤̣̿͐̈á̴͍̻̰͈̭̱̳͓͈̖̹̯͓̦̦͔͍̮̱̂͆͗̔̈́͑͂͆̉̃̑̏̓́̈́́̔́͑̚̕͜͝n̶͕̳͓̽̎͋̈́̊̌͋̾̀͑̚s̷̢̤̬͙͔̬͓͊̎̃͋̂͌̋̍̉̓̋̅͋̈́̅́̇͗̕͘̚͝͠͝.̷̨̛͖͓̫͎̥̰̂̓̀͛̊̍̎͊̀͘͘̚͝ ̷̠̰͙͍̥͇̥͇̱̭̭̥̄́͂͌̅̚͜Ļ̴̼̳̟̩̩̗̼͇̦̫̹̝̞͙͒͂͋̇̆ͅe̵̛̝̩͙̣͕̞͎͐̈́̎̈́̇̽̽̊̏̉̓͗̆̽̓̍̕̕ą̴̨̞̘̲̬͙̳͚̪̬̤̝̞͔̭̠̲̑̍̌͜͠v̵̢̡̧̜̺̘̻̭̭̲̣͓̩͕̩̹͈̖̘̼̟̥͙̑̋̋̓̏̀͂̒͂͛̌͑̏̇̃̚͘͘͝͠ͅé̴̛̝̓͆͛̍̒͛̎̅̎͌͌̊̈̀̊̊͑̊̕͝͠i̴͆̈́̓̂͘ͅn̷̨͓̫͎̠͈̥̟̻͓̹̳͍̘̜̥̜̳͙̟͚͉̮̊͆͒̈́̎̐̑́͐̎̏͛̑̕͝͠g̵͈͓͚̖̭̯̯̼̹̞͓͚̥̬̼͇̝͘ ̶̫͋̒u̷͚̼̰̐̀̇͌̇̽̏͒̉͆̈̽͋̅̾͘̚̚̚͝͝͠͠ͅș̵̗͙̹͎̼͖̯͈̝͈̘͇͎̦̈̈͑̑͑͊̕ ̴͕̩͚͕̣̤̔̃͂̂̅̏̒̐̐̉͘͘͜͝͝t̶̡̩̭̫̦̦̣̘̦̭̻̹̝͍̫̜̄̊̀̓̆͒͒̀̆̈́̂̕͘͠͝ǫ̴̧̱̠̭̻̥̭̯̝̪̪̪̖̝̫̗̹̬̬̯̋̓̏̋̈̒̕̕͝͝ͅͅͅ ̸̢̨̨̬̗̹͔͍̥̰̝̩̣̬͎̪̮̮̪̬̦̪̎̆̈́̽̾̏̀͗͐͂͋̑̅̇̍̓̇̎͝͠ṫ̵̞͔̰̥̼̞͎͚̳̱̳͕̘͇̝̦̲̮̞͔̇͌͒͑̎̿̋͋̃̑͐̚͝ͅa̴̧̰͓͔̬̗̥͇͕̞͍̝̯̖͌̍̌̍́k̶̨̨̢̡̜̘̩̙̲̫̭̗̹͚̰̜͈̪̇͜͜ę̸̛̘͇͔͉̖̖͔̣͉̒̒̾̅̆͋ ̸̞̟̒̑̍͋͐̏͛̎͗̊̈́̏̈́́̐͐̆͘ţ̴̧̝̫̹̺̙̱̩̥͓̝̝̜̓̈̔̋͌̈̊̏̇́̍̊͋̉̐͑͛͌̀̚͘̕͘͜h̶͔͉̼̦͕̝̳̣͇͚̙̫͉̗̦͔͍̫̿͂̇̈́̈̓̏͒̌͜ḙ̵̖̤͙̰̺̗̠̼͖͉̲̦̗͎̩͒̎̾̽̍̑̈̀̄̋̐̔̐͝ ̶̨̖̯̗̭̪̯̣̼̪̪͇̝̽͐e̵̻͚̬̳̦̼̤̬̦̝̭̪͇̩̱̲͋͆̽̂̽͜ą̵͔̌̏r̶̮͇̘͙̀̈́̓̑͆̔̐̈͗͒̃̇̅̀͘͝t̶̡̨̨̝͓̠̼̝̟͙͈̫͔̠͂̓͒̄͝ͅḥ̴̢̛͖͔͇̟̗͇͚̱̫͑̀̿̒̉͌̈́͗͆̌͒͛̒̇͘̕͜͝͝͝͝ ̷̡̛̙̳̜̜̬̯̼͒̈̎́̎́͗̂̿͛̌̈́̓̎̈͗̑̇̔̀̚͝͝͝f̷̨͉͕̬̝͕̳̠̝̜̻̺̮̺̦̱̩̰̪̯̬̔̅r̵̝͇͐́͑ơ̶̹̬̯̫̲̦̣̬̻̊̑̄͆͌̈͗̒̈́̈́m̶̧̧̧̮̖̼͕̱͕̬̼̭͇̂͆͌̐̌͋̊͘͘͠ ̴̧̧͉̜̤͈̻̰̄̈́͋̂̐̉͐̏͌͛͋̿̈́͗̓̚͠t̴̫͕͇̲͖̯̀͊́̀̓́̔͘ͅh̶̢̢̡̛͚̞̻̺͎̫͉̗̪̰̦̲̬̫̻̙͍̅͗̽̆̉̓͜ͅe̷̟̟̋̐̽̃̄́͆͆́̆͆̕į̵͚̪̜̖̼̲͔̘͍͖̭̼͕͎̖̰̱͔̆̎̄̚ŗ̵̧̡̧̧̛̯̖̯̫͍̝̮̗̜̱̞͙͆̿̐̑̐͂́̐͐̓̆̀͌͠͝͝ͅ ̵̖̄̌̏̂̂́͋̈́̑̓͛͐̏͌̔̔͌̅͝͝d̶̨̨̖̖̬̯̣̿̈́͑͛̓̃̂̈́̿̀̌͘̕͠͝͠ę̵͙̼̼̜̦̟̺͂́̔̈͛̅̒̓͌̈́̀̐̈̍̆͋̋ş̷̣͎̏̂ĭ̷̢̮̦͚̗̰̘̭̣̟̞̤̦̼̹̭̣̗͈̖̀̽̍̃̋̈́̆̊̇̆̿̔̒̍́͊͌̎̀̓̕͘̕͠c̷̨̥̦͍͔̤̫̲͉̖̔͆̀̄̒̽̀̑͛̀͑́̋̎͗̓͒͋̕̚̚͘͝͝͝ř̸̭̳̤̪̖̯̖̭̮̦̩̞̙̇̈́̓͛̏ͅa̵̛̪̺͚̯̱͇̫͍̞̰̟̤͑͐̒͊͊́͆́̕͘͜͝t̶̡̥̞̘̻̹̱͎͈̱͈͉̘̗͔̦͔̫͙͖͇̗̄͆̎̆́̇̅̀̆̏̋̓̉͋̂͛͜͠e̷̢̨̢̡̛͍͈̝͇̦̤͔̯͕͙͔͈̝̼̯͔̔͑̇͌̽̌̏̎̀̌͑d̶̡̨̛̛̞͎̖͔̠̲̖͚̯̲͓̼̟̠͙̭̦̉͗̂̔͊͊̎̂̂͑̿̀̀͑͑͛̾̌͝͝͝ ̸̧̹̺̤̭̼̰̰̺͖̠̱͖̖͍͎̤̻̠͖̏̍̋̑̃͆̾͆́̆̽̎̈́̋͗͒̂̕̕̕̕͘͝͝ͅċ̷̡̣̺͔̣͈͉̪͎͈̩͚̦͗̍̔͛́̿̿͂̓̾͋̅̈́̎͆͆͗̑̓̓͝o̷̢̡̡̼̱̹̩͕̗̦̮̲͖̪̠͎̳̱̺̥̤̠̅̀͂̊ͅŗ̵̢̨̢̢̛̦̪̦͙̟̠͎̺͓̱̓͂̈́̈́̔̉̃̏̐̽̈́̋͗́̐̊̅͘͘͝͠ͅͅͅp̸̢̨̧̧̝͔͎͉̘͓̪̘̖̺͓͍̟̤͈̬͕͇̪̯̈́̽̍̋͐̂̅̿̂̋̕ͅs̵̛̛̖̖̼̯̠͚͔͚̥̠̳̮̞̥͓̜̰͖̳̗͔̈́͌͊̍́͌̍͋̐̋̕̕̚͝ẹ̷̯͚̰͓̪͖̾͝͝s̶̡͉̩̱̘͔̤͚̤̞̜̺̖̯̟̤̖̝̹͉̙̹͖̺͒͋͒̋̅̃̈̈̂̄̓͛͑̔̕͝.̸͕͔̠̭̖͚̪̘̤̮͎̿̐̒̉̇̋̎̔͒̀͒\"̸̧̛̠̣̤͇̫͔͕͚̪̠̖͇̭̼̯̞̳̯̿͆̾̍͆̂̀̕̕̕͝͝͝͝͝ͅ\n\n\n[[CONTINUE|Text Part 6]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "Text Part 6",
          "original": "[[CONTINUE|Text Part 6]]"
        }
      ],
      "hooks": [],
      "cleanText": "\"̸̡͈̦̳̫̃̒̌̎̿͘T̸̨̨̛̛̙̮̼͈̦̺̗̀͐̄̑͗̎̏͌̓͌̑͑̑̕͝͠h̷̜̤̥̦͓̳͇̣̹̮̻͉̣̼͇͋̂̌̽̄̑̄̋̇͑̽̊͊̊́͘͝e̶̡̡̧̧̫̭̥̣̫̫̪̣͎̳̭͉̻͖̮͕̼̖̝̅̔̽̾̒̅͐͋͋̎̕͝͠n̴̛̰̱̳̰͇̳̫̥̮̹̪̎̏͛̃̾̊̈́͑̔̄̾̏̕̕̕̚̕͝ ̶̧̞̮͍̝͈̱͈͓̀̃̊̓̊̔͘͝͠͝͝ͅt̷̜̺͎̗͊̾̈́̽̾͒̽̃̆͋̃̅͋̀̚͜͝ͅȟ̷̛̞͉͎̥͍̥̩̘̜͆̉͑͜ͅę̴̢̦͎͓̗̞͉̞̙̟͕̱̟͙̠̙́̉̋̅̓̂̓̈́̅͛̃̑̈́̽̔̍̊͋̽͝ ̸̧̧̨̹͉̰̙̞̰̞͙̩͙͎̯̮̘̓͆̽̾͊͗̓̽̿̇̽̓͒͋̌́͐̇͋̇͘͘̕͝c̸̲̋͋̈́̈́̔̄̂̓̓͊͌͒ͅr̵̨̨̨̢̢͙̹̝̝̳͔͈̲̗͉̪͚̙̩̫̯̪̞͂̏́͗̓͗̋̆ę̷̲̙̖͇͚͉̹̼͈͈̟͇̭̬̼̰̝͖̩̉̈́͆̑̎̒̎̏̌̈̅̄͒̎̿͘̕̚͝ͅͅa̵̧̨̧̛̼̟̤̜̗͚̜͈̭͖̲͖̳͇̓̏̊̆͌̏̇̎̈́̆́̓̈͐͋̈́́̒͜͠t̷̛̟̱̪̠͇̲̞͓̤͖̱̭̫̒̎̓͛͋̿̈́͛̌̓̇̉͑̒͛̇̾̎̉͆͘͘͜ò̸̢̧̓͐̽̇́͋̿͆̎̕̕r̶̨̹̹̲͓̭̉̓̉̂̆̀̽͐̈́̅̉̆́̆̊͋̒͐̂͋͘͝s̵̨̖̪͚̬̜͇̻̞͓̪̬̜̘̬̲̦̉͜͜ͅͅ ̵̛̜͔̻̻͕̼̙̺͚̰̰͍̹̂̆̓̏̌͋͗̐ở̸̛̘̜͇͒͒̈́́̌̆̊̋̑͆̚f̷̯̼̮̦͈̹͖͍̦̑́́̂̌̐̆̀̿̑͒͐̓̔͊̄́̈̎̏̔̈͑̕͠ ̴̡̧̼̭̣̫͉̣̹͙̟̟͖̼͙͉̮̯̖̻̠͕̭͇͒͊͛͑́͛̊̿̋̈́̒͛͐̀̓͗͐̓͆͘͠͝T̸̲̯̆͂h̷̡̢̡̡̛̘͇̹͙̰̰͍̳̟̮̝̪͉͕̯͈͍̘̯̠̔̍̀̃͑̀̄̃͊͑̒͂͠e̷̢̢̙̫̹͙̹̱̟̖̯͚̖͉̞͍͈̼̜͙̪̥̜͂̆͆̀͆̀͐̏̓̔̀̐͂̕̕̚͠͝͝ͅ ̸̧͍͓̟̻̣̻͉̥͖̪̟̓͜͠Ơ̵̧̥̯̝̱̯̻̞̺̘̜̓̓̅̽̂̇̀̅͛͛̈́̑͑͌̀̚͜͝͠l̵̨̧̨̢̛͎̯͒͛͌̾͋̄̈́̍͐̔̐̔͘͝͠d̷̨͔̙̯̦͇̲̝̻̾̒̀̑̏̌̓́͝ ̶̨̛̥̼͇̭̙̯̀̀̆̅͗̂͝Ỏ̵̧͎̺̜̱̪̱̈͂n̶̨̡̯̤̟̭͔̰̰̜͍̘̺͉͈̝̰̮̝̻̜̯̬͂͗̔̈̎͂͒̈́͌̌͝e̶̳̣͓͉̹̤̘̰͇̲̯̳̙͎̞͚̊̓̈́̈́̏͗͋͜ ̶̹̩̺̹͚̫̦̣̯̲͎̼̭̯͚̰̭̹͕͎̙͖̭̂̅̌̅͐̉̎̂̽̑͒͜͜͝͝ẅ̴̨̢̜̻̣͓̪͙̝̳̪̱͈̟̺̯͕̦̖̹̑̑̉̀̉͆̊͗̓o̶͕̪̝̻͓̦̝̓͑u̴͚̒̅̃̌̈́͛̂̀̅͗̈́́͌͆̚͝͠ͅl̴͍̳̱̭̣̥̣̰̺̝̳̍̔̀̾͒̾̒͜͝d̶͙̮̪̦̰̯͆͑̋͋̑́̆̀͆̐̄͘͝ ̷̧̡̡̛͍̦̮̪͉̥̠̙͓̣͉̤̭̖͔͆͋̓̿̾͋͊͂͛͗̊̈́͘͘͝t̴̢̨̢͖̗̤̹͓̦̪̭̳͈͉̖̗̩̯̘̞͓̄̅̋̂̀̀̆̽͋̎̀͌͒̾̎̍̕͜͠ͅͅḩ̶̦͚̺̱̪̊͑̐͊̓̈̈́̀͋̎̍̓̀͋̒̕͜͜ͅé̴͔̥͙̣͍̞̝̹̺̥̫̬͌̈́͐ń̷̨̨̛͔̏̐̓̓͗͂̒̓̚͘͝͝ ̴̢̨̦͖͚̥̼͈̺̤̗͖͕̰̙̜͙͕̣̱̬̓̈́͑̏̌̕͘͜͜͝ḏ̵̛̻̙̒̌̽̓̐̎̽̈́̾͂̏̑̓̚͝e̷̡̞͓͙̞͔̯͓̖̳̝̞̦̹͔͈̿s̸̖̼͝ȩ̷̨̢̘̠̝͕͚̌̿̌̐̂͆̽͑̒͌͘͠n̵̨̧͉̖̦̫̮͇̜̞̳̬͚̘̲͓̏ͅď̶̨̧̛̮͕̤̘̯̩̯͔̖̺̠̜͕̟̩̣̬͈͖̣̎̈̾̈́̇͐̍̄̌̚ ̷̛̠̲̣̎̌͛̈́͗̀̓͛͆͂͒̍͋̏́͒͘̕͝͝f̴̧̗̺̙͈͇̠̙̠̉̈́͑̊̏͋̈͒͛̇̽́̋̍͝ͅr̷̨̳̪̪̖͖̹̹̻͉̔̈̿́͛̍̈́̐̌̒̈͑͂̿́́̉́̚̚͘͝͠o̸͖͈̞͚̼̬̤̼̹̦͆͋͒̑͐̐̃̋́̒̅̑͠m̶̧̡͚̖̼̻̣̰̦̝͈̦̤̺͉̗̠̩͎̌͂̍̓̀̓̍͗͌̓͒̿̓͋̒̃͌̃̑́̚͘̕͝ ̸̢̟̯̩̭͙͈̣̮̬̞͕̘̗̟̤͈̠̮̣̫̟̩̌̓̓̒̈́͒̊͐̔̚t̶̟̪͎͕͉͋̈́̎̎̄̀̃̌̊͌͊̄̃̋̊̈́̆͠ͅh̶̛̛̹̐̌̌̈̂̎͛͑̈̒͊̓̍̈̀͛̒̀̊̍̕͝͠è̸̹͓̤͎̌̈́̾́̈́̐̅ͅ ̸̡̡̨̨̖͔̩̱̠̥̺̩̦̝̩̺͙̩̣̙͔̉͂̓̌͂͊͂̌̀͐́̓͘͝s̴̡̹͍̦͈̮̗̬̞͓̐̿̿̈́k̵̗͕̺̟̯͓͗̾́̐͂̈́͊̅̆̋̋͐̊̈́̓͆͊̕͘̕̚̕͠ͅy̸̯͉͉̬̗̣̿̿̇̆̋̒̍̐̉͒͋̉͆̋̽̔͂͒̽̿͊̓́̐͜͝ͅͅs̶̛͖͎̹̯̓̈́̔͗̈,̵̡̡̢̨̧̲̮̩͖̼͈͈͓̹̺̭̞̟̞̩̳̥̖̈́̇̒̐̅̎̀͑̓̔̕̚͘͘͘͜͜͝͝͝ ̴̜͉̳͉͉̫̣̮͛̔̌́̀̓̾̀̋͗͋̍̾͆̑̏̌̓̎̐͘̚̚͠͝ţ̸̧̨̮̩̮̜̹̳͓̌̂̓̍́̈́̕͜h̶̡̦̝̺̠̳̻̎̓̌̕e̴̛̲͍̪͛̅̽̀̓ý̸̧̻̠͎̝̤͓̝̖̘̤͔̰͖͒̀̎͌͆͛͐̓͂̎͗́̾͒͌̅̾̽̀̈́̚̕͜ ̸͉͕͙̜͕͍̘̦̗̖̻͖͓̘͕͇̲̻̳̟̮͋͆̏̈́͐̊̌̓͑̃̈̐̇͂́̽̈́̃́̚͘w̴̨̺̙͓̤̠͎̖͊̀̊̄̄̒̎̃̍o̶̰͇̟̣͎̜͓̗̭͛͐̋̐͐̐̊̎̉ư̷͔̝̜͉̹̗͖̞̺͇͖̗̲͙̑͗̌̀͂̉̎́̌̑́̃͛͊́̓̍̆̌̕̚̕͝͠ͅḻ̷̛̼̘̱͉͕̭͉̙͈͙͉̬̪͇̩̭̠̥͖̻͍͊̈͒̀̅̌̾̓ͅͅd̶̨̛̞̜̙̼̳̦̳̱͍͍̪̯͌̔͊̊̾̄͑̀̈́̈́̈͒̊͒̓́̌͂̈́͒̆̕͜ͅ ̸̢̼͕̰̱͉̰̹̬̙̭̳͙͖̋͛̓̌ͅͅc̶̢͍̞̼͉̮̜̺̗̝͚̲̳̤̪̼̒͌̂̈́͆͂͒́͊͊̈́̓̋̚ô̶̙̤͍͔͖͍͚̥̝̖̞̠͊̅̏̉̇͂́͛̌́̂̈̿́̾͑͘̕̕͠͝͝͠m̶̨̡̧̛̙̞͉͇̲̩̙͉̯̝̖̹̖̯̖̘̲̼̘̪̋̉̈̓̀̓̌̅̈́̑̊́̒̓̓͛͐̒̓̌͑͘͜e̸̡̧̢͍̪̥̙͇̬͌̅͑̾̑̓̀̿͐̈́̏͝ ̸̡̛̞̘̲̘̳̪̳̘͍̻̼̣̥̟̔̑̎͊̇̄͆̃͝ͅͅt̶̢̛͕̙͉̝̹͕͖͎̲͗̌̀̈̏̌͒̀͐͂͗̈́̂̕͘͠ö̸̢̨͍̫͕͙̫̳̮̖̫̝͎̭͎͈̣̖͓̻̞̩̜̦̳́̏͒͗͗̊͌̑̓̀̀̈́̆̍̾͆͌͐̇̈̀ ̸̦̅̇̇̏͒̈́̈̊̀͂̆͑̒̍̇̀͛̅̅͋̉̇b̸̧̝͓͎͖͔̦̻̯̱̪̟̾͂͆͒̈̊̏͑̀̇̑̓̋̑̓͌̋̀̚̕͘l̸̰̺͓̇͌̅̃͒̈̏̅̐̀̒̏̂̐͂̕̚̚̚͝͝ě̸̺̪̥̮̣̤͕͔̹̫͚̞̓̋͋̽͂̏̄̆̓̈́͝s̷̨̨͍͖̪͓̞̙̱̣̻̙̰̮͒͜͠s̵̨͚̪̜̤͙̯̫͍͎̥̻̙̪͚̖̀̐̊͠ ̸̡̡͔̝̥̩̤̟̥͈͇͇͆̈́͌h̶̢̛̗͕͇͍͓͎̩̻͖̘̘͎̰̟̅̐̈́̾̄̏͐̓̎̓͆̽̎̑̚ų̵̨̝̟̰̤̞̞͕̺̼̺̼̹̯̩̝͍͎̦̝̄̔̋̊͌̽̑͂̒̿̅̄̃͘͜͜͜͝ṁ̶͈͈͈̗̅̾͆͊̉̕a̷̪̯͓̙̣̥̪̥̺͍̞̲̯̙͈̮̘̝̅́̎͂̃̀̓̅͑̓̑͒̅̉́̎́͊̍̕͜͝͠͝͝͝ͅň̶̦͍͎͌̈́̊i̸̡̠̣͍̗̩͈̪̭̬̖̘̹̥̮̐́ͅͅt̵̡̧̮̲̯̠̳̩̟̦̺͈͈̩̠̻͎̳̻̱̫̖̩̜͛͗͊̄̽̎̂͋͂̕͝͝y̸̢̛͖̯̗̗͕̘͍͚̟͚̞͈̮̥̝̳̘̫͉͐́͊͌̀̎̓̎̓̆͂̂̀͆̓̄͌͋͐͘̚̚͝.̵̨̧̛͉̻͎̩̪̯̙̞̽̋̏͂̂͌̂̚͜͜͝ͅ ̵̧̛͖͔̹̤̜̝̝͂̈́̓͋̎̓̂͂͘B̶̥̟̥͙́͠ȕ̵̡̞͈̣͔̤̘̤̯̣̬̟̬͇̳̙͋͛̏̈͝t̷̛̠̖̬̘̞̜͔̳́͑̆͆̇͂̈́̌̕͝͝͝͝,̴̨͈̫̮̦̤̩̞̟͖̜͇͍̦̳̘͓͚̮̓̀̊̒̿̔̕͠ ̷̡̛̰̮̥̗̠̫̩̥̯̩̲̺͇̩̜͚̩̹̹̝̄̈̅̒͛̎̓̿͊̊͑̕t̵̢̧͚̬̳̫̞̮̗̮̏̋͒͌̀̿͒̓̇͐̆͑̒̈̊̂͐͆͊͐̇̉̚͝h̴̻͍͖̟̹̪͑̚ȩ̸̛̞̤̩̞̝̼́̽̐͆̂̾̍͜͠͠ ̶̫̼͉̘̤̞̗̙͙̩̟̙̳̄͒͗̄̌̈̔̐̔͊͗͗̏̓̑́͘d̸̨̧̧͉̜̥̬͉̮̰̠̠͍̳̟̩̱̩͍͕͇͇͓̍̔̀̈́̅͑̂̈́̆̇͋́̎̾͛͒̐͊̚͠͠͠ę̵̡͙̪̬͓̬̤̙̙̯͚́́̎̒̆́͂͗̄̽́̕͠ş̶̢̞̻̳̼͚̞̞͚̼̤̋̀̔̈́̄̓͠ģ̷̡̟̞̮̜̤̞̖̹̞̘̖͍͖̳̘̪̜̤͑͗̏̉̍̆̋͑͒̀̈́̇̂̐̅̾̾̿̚͝u̷̡̦͕̫̱͚͓͕̜͎͉̫̲̞̦̭̲̇̌͆͠ş̷̨̫͉̳̹̜̣̰̜̺̣̺̘̫̻̓̎̃̏́̉͑͐̈́̕͜ț̴̡̛̦͍̫̣̜͙̘̮̠͙̭̘̦̪͖̖̰̭̬̲̥̿̑̉̆̈́͂̓̏͑̔͛̀̍̾̾̏͆̉̕̚̚̕͝͝i̷̢͓̮͙͈̱̫̞̩͒͆̈͒̈́̾̑͒̄̿͗̐̏̋̈́̇̾̕͘ņ̶̢̝̹͔̳̜̲̳̬̪̿̒̐̈́̾̾̓̅̓̈́̍̿̃̾͠g̵̢͇̘͚̱͈͇̦͐̂̒́̄̓̑̅͘ͅ ̶̢̛̦͙̠͚͕͙͈̤́̃͂̓̿̃̈́̄͐̈́c̸̢̨͎͙̣͖̺̰̗̖͈̙̩͚͍͙̭̰̾̈́͑͊͑̒͝r̶̢̧̢̛̗͍̺͙͉̯͇̖̯̙̣͇̻̫͕͚̗͇̘̈́̆̌͋̇̈̋͛̄͛̓̆̈́̆̿̾̈͗̕͝ȩ̴͎̲̖̦̹̪̱̙̀̒̊̾̌̓ť̴̪̥̣̗̦̹̟̪̭̹̮̰͙̹͓̞͖̩̃̀̉̏̍̓͌̾͝ͅo̷̼̝̣͓̱̤̾̒͒̌͆͆̈͛̔̒͘͘͜͝ń̵̡̧̟̮͕̼̜̼̼̟͍̳̃͋́͐͑̄̑s̵̞̲̠̘̞͈̯̜͐̑̃̽̽̓̂̆̃̂̕͠͝ ̸̨͙͚̳͍̰͒́̋̾̅̓̈́̓̽̈́̑́́̽̕͠͝ǫ̶̙̯̘͖͕͖̟̙͍̻̖͉̫̳͕̬͚̩͗̾̃́́̔̽̿̽̆͗̍͐̀̓̋̕͜͝͝ͅf̷̛̛̼͕̜͇̰̬̦͉̫̖̠̳̙̪͕̜̲̖̫̤͍͉̓́̓̓̿͒̾̿̂̇̂̀͋̀͋̽͘̕͝͝ ̷͈̺̦̠̦͈́͛̓̂̐̄̎̉̏͛͆́͑͋́ţ̸͉̼̙̰͉̖̼̰̖̔̐̋̉̓̓̈́̍́͂̈́ḧ̸̨̠͇̠̱͓̥̖̝̭͕̤̝̟̰͚̤͈̗͚̔͛̋̊́̿̊̔͊͝ͅé̴͇̥̞̫̠̥̹͍͆̂͐̆͛͊̂̄̀͗̈́͊͊̂̂͒̋̚͝͝ ̸̧̦̻̺̳̟̙͖͕͉̗̮̣͗̔͐̒͒̈́͋̔̇̍̉͋͘̚͝e̷̬̎ą̷̢̱͎͎̱̱͚͈͇̻̲̼̦̠̬͇̗̼̻͇̼̣̙͋̿͌̀̽̽ͅr̴̜̤̮̝͔͕͙̗̮̥͔̜̳̖̳̬̥̣̞̋́͐́͗͒́͌̆̆̉́̐̒͑͐̒̾͝ͅͅt̷̩͙͈̭̟̠̫͑̂̐̈́̊̂̊̾̅͂̉̇̄͗̀͆̀̒͘͝ḧ̸̡̪̳̱͈̬̺̖̬͖̠̺̦̝̈́̄͗̅͌̾̐͌͊͘ ̶̢̛̮̣̾̓͗͐̀͗̆̊̾̆̎͗̈̒̚͘͝ͅw̶͙̼̞̃̽̊͋́́͆͒̓̊̅̀̓̏̓̅̓̕͠͝͠ǫ̷͚͚͇̫̣̘͉̞̠͖̦̟͔̲̣͇̟́̉̈́̂ͅú̷̢͓̳͚͚̱̥̻͈̣̖̣̱̲̗̱̖̙͐̎̉̿̉͊̇̾̋̏̎̍͒̋̏̈̇̓͘̚͜l̶̢̦̯̳̮̫̞̰͙͖̥̠̤̺̙̻̘̥̖̩͐̈͂̒̈́̋͜͜d̶̛̟̺̦̖̗̲͍̒͛̎̏̒͐͌͂̀́̅̀̿̀̂ ̸̱̗͖̼͙͈̭̖̬̩̥͕̟̱̻̈́̽͂͐́̍̔͗͐̐̑͋͑̈́͐̈́͠͝r̴̨̛̘̖̪̳̀́̃͌͒̒̉̃̀̿͌̒̊̽̍͘͝͝e̴̢̡̧̪̘̙̱̙̺͉̔̔̔͐̔̀̕͝͝f̶̨̡̮̠̻̰̠͍̘̪̱͔̰̗̯̯̖̤͖̯͑̊̎̈́̋̂͠ų̸̧̧̙̯̺̫̩̰̣̖͚̰̙̥͙̈́̔̈͐̂̈́̈̽̕͝͝s̸̲̖̦̿̓̅͑̾́͌̔̑̅̔̋̂̽̾̿̋͂̚̚͘̚͝͝ę̸̛͚̭̖̰̲͓̲͓̻̪̭̹̯͎̫̇́͛̆̂̿͌͆͗̈́͆̋̽͊̄̋̈́̓̓̽̕̚̕͝ͅ ̶̧̢̛̻̥͔̫̻̗̣͔͎͚̼̗͖̱͉̫͓̩͗̉̔͑͊̍͜t̸͉͇͛̂̐͊̽̆̀͆͗͆h̶̗̖̝̠̥͕̃̒̈́͐̏̕ẽ̵̢̲̘͖̟̫̬̥̫͚͈̦͎̺͓͕̖̫͖͎̉̔̐̈́͂̆ͅͅͅḿ̸̢͈̟̞͇͔͓̱̳̂͂͂͊̓͑͒̇̐̏̉͒͑̍͛̽͘͝͝͠.̵̡̓͋ ̸̢̨̳̹͔̯̲̲̖̟̱̲̩͎̖̏̍̄̈́̈́̈́̍́̊͂̚͘A̶̧̘̩͗̑͛̇́͐̄̋̆̑͐̾́͗̄̐̽͊͘͘s̴̨̥̫͈̰̩̺͍̟̜͈͙͒͌͂̐͂̂͂͊̇̇͜͝͝͠ȟ̷̨͔̯͉̟̐̉͊̆̄̏́̓̚̕ͅã̵͈̼̻̘͙͙̻̈́̉̾̎̋̈́̾̎͑͐̾̒̈͆̏́̑̿̀̕͘͘͜͝͝m̴̘̤̣͔̣̯̰͇̤̠̠̹͎͚̏̈̊̽̆̌̾̈́͐͘̕͜e̷̢͖̟̼̭̭̺̯̐̈́̔͘͜͜ ̴̧̛̯͚̣̤͚̻̟̻͙̬͎̝̖̳͕̠̰͐͋͆̽̎͐͂͒̃͂́̀̉͋̕̚͜͜ͅt̴̡̧̠̖̰̣̹͓͎͈̱̥̲͒̍̽̈́́̈́͆͆h̶̢̧̻̠̘̤̝̠͔̭͖̭̦͉͉̭̹̩͖̗͍̦͈͉́̎̌͌͒͆͗̍̕͜e̸̢̫̹͉̜̅̐͆̑̃͐̈͆̀̿̀̔͊̄̋̚͝͠ͅs̴̡̛͕͉̍͂̆̎͐̊̏̿͛̈͋̋͗̆̈͋̇̋͘̕͜͠e̵̡̅͑̾́̈́͘ ̸̢̡̺̥̥̤̦̰̼̘̗̰̠͖̳̥͕̹̭͗̅̈́ͅḑ̴̢̛͚̘̞̭͇̰̖̫̮͓͉̻̜̼̘̗̪͇̰͕̖̇̀̐͂̒́͒̽̽̓̓̽̾̈͛͠i̶͔͉̫̘͖̱̗̓͛̉͋͠v̸̢̡͚͕͚͍̦̟̭̰̓̏͆̓̐͝͝í̶̧͉̯͍̫̻͉͉̬͍̖̫̼͙͇̖̫͚̰̽̃̂̕n̷̘̳̖͓͇͚͖̬͙̗̥̬̹̩̘̠̩͎̥̘̱͉͉͛̐̔̎͆̒̍̇́̽̊̍̈͌̕̕͝͝ë̶̙̹̖̳̱̹̮̗͖͇́̓̊̀̍̅̋̈́̈́̚̚͝͠ ̶̧̨̨̢̢̡̨̛̘̩͎̘̱̪̪̼͍͍̻̭̔̅́̽̉̃̆ͅb̴̪̹̲̈́͐̔̈́̆̀̈́̄̈́̇̏̾ę̸̧̡͚̱̗͍̪̘̼͚̟̯̞̪̩͈̹̦̘̥͛̈́̽͛̆̕ḯ̷̛̥̻̼̖̺̙̉͗͆͌͐̓̈̿͒͑̂̅͋̂̌̆̍̈́̚͜͠ṉ̷̡̡̹͇̖̥͍̪̟̘̫͕̙̳͎͚̳̞̻̭̆̒͊̂͆̌͛̃̒̽͆̅͊̀̄̌̕͜ǧ̵̼̰̼̻̠͕͓̲̯͉̖̣̟͇̈́̀̓̅͑̋̾̍̈́̈̾̔͠s̷̗̲̰͉̬͔̼̤̰͕̰̱͖̹̺̘͓͙̽͋͜ ̶̝͔̫̤͍͙̱̓͊͑̀͑̋̌̆̕͝ẉ̶̡̛̗̤̫̫̰̮̳̦̩̤͇̗͚͉̬̜̫͖͚͙̬̩̊̀̿͊͂̈̂̔͐͑̈́̒̆͂̋̀͗͊̎́͘̚̕͝ö̶̡̨̼̼͓͇́͋́ṳ̶̢̨̧̤̩͈̮͖̗̳̰͔̟͍̬͎̥̟̩̼̦́̈́̇̽̊̎̄͆̓̉̀̑́̆̕͘͘̕͜͝l̴͚̙̣͖̤͈̗͖̞̮͙̫̖͖̞̤̮̫̤̲̬͒͆̈́̈́͆̚͜͠ͅd̶̨̢̹̼̲͖͖̺͗̑͗̓́͐͆́̿̅ ̵̝̆̋̽̉̍̃͗́̿̅͋̓͋͠͝͝d̷̲̗̓̇̕e̷̡̧̨̞͍͙̳̞̤̺̱͓̟̤̺͈̐ͅs̴͖͈̥̗̠͓͙͍̟̥̝͔͚̲͌̌̏̑͊͘ͅt̸̙͉̦̗͙͖͈͍͎̳̞͙̱̘̏͆͊̋͂͂͑́̌̀͂̀̈́͠͠͠r̸̡̧̨̧̢̥͖̹̗̤̦̻͈̜̯̭̤͎̝͖̋̄̾͌̀̑̑̒̓͑̈͂̓̅̎͊͊͘̕̕ǫ̵̼̮̪̭͍̦͖̤̣͉̖͓̠̗̲̞̲̱̯͌ͅý̵̢̜̪̪͎͖̩͙̜͈̟̖̦̗̤̹̰̤̰̯̼̀̍̆̇͗̈́̊́̀͆͗̾̇͠͝ͅͅͅ ̷̡̛̛̱͖̩̳͖̗̼̫͈̣̺̘̥͎̪̟̬͙̟̪͍͎̋̋̋́͝ẗ̸̛̝̰͖̗̲́̀̌̑̀̽͗͒̀̌̔̋̈́̑͂̋͘̕̕͠͝͝h̸̗̞̼̗̬̗̺̯͚̻̀͐͐̀͐̍͛̾̆̊̈́̉̉͑́̓̎͝e̵̳̝͈̳̬̞̘̘̰̙̙̭̟͉̥͇̗̥̐̂̄̓͜͝ ̵̢͕̥̘̠̯̗̎̀̈́̈́̑̀h̷̨̡̡̡̛̛͎̜̙̜̮̲͔̺͚͕̩̝͒̏̅̆͐̎͑̄̋̎͝͝u̴̟̟̻͓̇͐͋̑̌͗̀̓͋̀̚̚m̴̧̢̧̮͍̘̫̬̱͕̮̲͎̬͈̬̹͙̣̮̰̟̤̣̿͐̈á̴͍̻̰͈̭̱̳͓͈̖̹̯͓̦̦͔͍̮̱̂͆͗̔̈́͑͂͆̉̃̑̏̓́̈́́̔́͑̚̕͜͝n̶͕̳͓̽̎͋̈́̊̌͋̾̀͑̚s̷̢̤̬͙͔̬͓͊̎̃͋̂͌̋̍̉̓̋̅͋̈́̅́̇͗̕͘̚͝͠͝.̷̨̛͖͓̫͎̥̰̂̓̀͛̊̍̎͊̀͘͘̚͝ ̷̠̰͙͍̥͇̥͇̱̭̭̥̄́͂͌̅̚͜Ļ̴̼̳̟̩̩̗̼͇̦̫̹̝̞͙͒͂͋̇̆ͅe̵̛̝̩͙̣͕̞͎͐̈́̎̈́̇̽̽̊̏̉̓͗̆̽̓̍̕̕ą̴̨̞̘̲̬͙̳͚̪̬̤̝̞͔̭̠̲̑̍̌͜͠v̵̢̡̧̜̺̘̻̭̭̲̣͓̩͕̩̹͈̖̘̼̟̥͙̑̋̋̓̏̀͂̒͂͛̌͑̏̇̃̚͘͘͝͠ͅé̴̛̝̓͆͛̍̒͛̎̅̎͌͌̊̈̀̊̊͑̊̕͝͠i̴͆̈́̓̂͘ͅn̷̨͓̫͎̠͈̥̟̻͓̹̳͍̘̜̥̜̳͙̟͚͉̮̊͆͒̈́̎̐̑́͐̎̏͛̑̕͝͠g̵͈͓͚̖̭̯̯̼̹̞͓͚̥̬̼͇̝͘ ̶̫͋̒u̷͚̼̰̐̀̇͌̇̽̏͒̉͆̈̽͋̅̾͘̚̚̚͝͝͠͠ͅș̵̗͙̹͎̼͖̯͈̝͈̘͇͎̦̈̈͑̑͑͊̕ ̴͕̩͚͕̣̤̔̃͂̂̅̏̒̐̐̉͘͘͜͝͝t̶̡̩̭̫̦̦̣̘̦̭̻̹̝͍̫̜̄̊̀̓̆͒͒̀̆̈́̂̕͘͠͝ǫ̴̧̱̠̭̻̥̭̯̝̪̪̪̖̝̫̗̹̬̬̯̋̓̏̋̈̒̕̕͝͝ͅͅͅ ̸̢̨̨̬̗̹͔͍̥̰̝̩̣̬͎̪̮̮̪̬̦̪̎̆̈́̽̾̏̀͗͐͂͋̑̅̇̍̓̇̎͝͠ṫ̵̞͔̰̥̼̞͎͚̳̱̳͕̘͇̝̦̲̮̞͔̇͌͒͑̎̿̋͋̃̑͐̚͝ͅa̴̧̰͓͔̬̗̥͇͕̞͍̝̯̖͌̍̌̍́k̶̨̨̢̡̜̘̩̙̲̫̭̗̹͚̰̜͈̪̇͜͜ę̸̛̘͇͔͉̖̖͔̣͉̒̒̾̅̆͋ ̸̞̟̒̑̍͋͐̏͛̎͗̊̈́̏̈́́̐͐̆͘ţ̴̧̝̫̹̺̙̱̩̥͓̝̝̜̓̈̔̋͌̈̊̏̇́̍̊͋̉̐͑͛͌̀̚͘̕͘͜h̶͔͉̼̦͕̝̳̣͇͚̙̫͉̗̦͔͍̫̿͂̇̈́̈̓̏͒̌͜ḙ̵̖̤͙̰̺̗̠̼͖͉̲̦̗͎̩͒̎̾̽̍̑̈̀̄̋̐̔̐͝ ̶̨̖̯̗̭̪̯̣̼̪̪͇̝̽͐e̵̻͚̬̳̦̼̤̬̦̝̭̪͇̩̱̲͋͆̽̂̽͜ą̵͔̌̏r̶̮͇̘͙̀̈́̓̑͆̔̐̈͗͒̃̇̅̀͘͝t̶̡̨̨̝͓̠̼̝̟͙͈̫͔̠͂̓͒̄͝ͅḥ̴̢̛͖͔͇̟̗͇͚̱̫͑̀̿̒̉͌̈́͗͆̌͒͛̒̇͘̕͜͝͝͝͝ ̷̡̛̙̳̜̜̬̯̼͒̈̎́̎́͗̂̿͛̌̈́̓̎̈͗̑̇̔̀̚͝͝͝f̷̨͉͕̬̝͕̳̠̝̜̻̺̮̺̦̱̩̰̪̯̬̔̅r̵̝͇͐́͑ơ̶̹̬̯̫̲̦̣̬̻̊̑̄͆͌̈͗̒̈́̈́m̶̧̧̧̮̖̼͕̱͕̬̼̭͇̂͆͌̐̌͋̊͘͘͠ ̴̧̧͉̜̤͈̻̰̄̈́͋̂̐̉͐̏͌͛͋̿̈́͗̓̚͠t̴̫͕͇̲͖̯̀͊́̀̓́̔͘ͅh̶̢̢̡̛͚̞̻̺͎̫͉̗̪̰̦̲̬̫̻̙͍̅͗̽̆̉̓͜ͅe̷̟̟̋̐̽̃̄́͆͆́̆͆̕į̵͚̪̜̖̼̲͔̘͍͖̭̼͕͎̖̰̱͔̆̎̄̚ŗ̵̧̡̧̧̛̯̖̯̫͍̝̮̗̜̱̞͙͆̿̐̑̐͂́̐͐̓̆̀͌͠͝͝ͅ ̵̖̄̌̏̂̂́͋̈́̑̓͛͐̏͌̔̔͌̅͝͝d̶̨̨̖̖̬̯̣̿̈́͑͛̓̃̂̈́̿̀̌͘̕͠͝͠ę̵͙̼̼̜̦̟̺͂́̔̈͛̅̒̓͌̈́̀̐̈̍̆͋̋ş̷̣͎̏̂ĭ̷̢̮̦͚̗̰̘̭̣̟̞̤̦̼̹̭̣̗͈̖̀̽̍̃̋̈́̆̊̇̆̿̔̒̍́͊͌̎̀̓̕͘̕͠c̷̨̥̦͍͔̤̫̲͉̖̔͆̀̄̒̽̀̑͛̀͑́̋̎͗̓͒͋̕̚̚͘͝͝͝ř̸̭̳̤̪̖̯̖̭̮̦̩̞̙̇̈́̓͛̏ͅa̵̛̪̺͚̯̱͇̫͍̞̰̟̤͑͐̒͊͊́͆́̕͘͜͝t̶̡̥̞̘̻̹̱͎͈̱͈͉̘̗͔̦͔̫͙͖͇̗̄͆̎̆́̇̅̀̆̏̋̓̉͋̂͛͜͠e̷̢̨̢̡̛͍͈̝͇̦̤͔̯͕͙͔͈̝̼̯͔̔͑̇͌̽̌̏̎̀̌͑d̶̡̨̛̛̞͎̖͔̠̲̖͚̯̲͓̼̟̠͙̭̦̉͗̂̔͊͊̎̂̂͑̿̀̀͑͑͛̾̌͝͝͝ ̸̧̹̺̤̭̼̰̰̺͖̠̱͖̖͍͎̤̻̠͖̏̍̋̑̃͆̾͆́̆̽̎̈́̋͗͒̂̕̕̕̕͘͝͝ͅċ̷̡̣̺͔̣͈͉̪͎͈̩͚̦͗̍̔͛́̿̿͂̓̾͋̅̈́̎͆͆͗̑̓̓͝o̷̢̡̡̼̱̹̩͕̗̦̮̲͖̪̠͎̳̱̺̥̤̠̅̀͂̊ͅŗ̵̢̨̢̢̛̦̪̦͙̟̠͎̺͓̱̓͂̈́̈́̔̉̃̏̐̽̈́̋͗́̐̊̅͘͘͝͠ͅͅͅp̸̢̨̧̧̝͔͎͉̘͓̪̘̖̺͓͍̟̤͈̬͕͇̪̯̈́̽̍̋͐̂̅̿̂̋̕ͅs̵̛̛̖̖̼̯̠͚͔͚̥̠̳̮̞̥͓̜̰͖̳̗͔̈́͌͊̍́͌̍͋̐̋̕̕̚͝ẹ̷̯͚̰͓̪͖̾͝͝s̶̡͉̩̱̘͔̤͚̤̞̜̺̖̯̟̤̖̝̹͉̙̹͖̺͒͋͒̋̅̃̈̈̂̄̓͛͑̔̕͝.̸͕͔̠̭̖͚̪̘̤̮͎̿̐̒̉̇̋̎̔͒̀͒\"̸̧̛̠̣̤͇̫͔͕͚̪̠̖͇̭̼̯̞̳̯̿͆̾̍͆̂̀̕̕̕͝͝͝͝͝ͅ"
    },
    {
      "name": "Text Part 6",
      "tags": "",
      "id": "33",
	  "knowledge": 10,
	  "corruption": 10,
      "text": "S̵̪̀u̷̼͖͗c̷͇̀͌ḧ̴͉̭́̕ ̸̨̫̊f̴̻͛o̵͈͂̔ř̶͖b̶̝͛i̶̺̘̔̍d̶͙͋́ḏ̸̆ẹ̵̤̎ṋ̸͈̀ ̶͎̮͊k̴̫̆n̸̰͐ỏ̸̺̅w̴̻̚ĺ̸̘̎ě̵̘͓̉d̵̗̣̅̕g̷̭͊̀ȩ̵̰̒͘,̷̣̎ ̷͔͍̓́y̸̨̰̌͐o̷͎̖̊͝ȕ̷̼̈ ̸̜͂͗m̵̫̆ủ̵̘s̸̯͛t̸̯̞̾͑ ̴̼̈́h̸̞́̐ā̴̦͍̚v̵̰̾̑e̸̙̾͌ ̶̣̻̾̍m̶̗̳͝ȫ̴̡ŗ̵̱̌̈ē̷̠,̷̪̖̓̽ ̸̝̿̊ͅy̵̨͒o̶̽͜͝u̴̮͎̾ ̶̤̚m̷͙̓ụ̵̋s̴̙̊͌ṫ̶̺̩͑ ̵̻̟͛k̸͔̾̄e̴̮̽̅ę̵͈́p̴̪̖͊̚ ̷̮͕̓r̴͕̐̊e̸̯͒̾ä̵̝̫d̷̤͚̏i̵͙͎̎n̴͖͍͊g̷̈́͜.̴̢̻̎͘ ̴͎̔͒͜.\n\nY̵̡̬̟̰̩̾̋̌̅o̴͓̝͈͓̭̲̙̣͊͛̓̄̈́͛͜u̵͉͊̓̈́ ̶̡̧͍̱̯̙̠̣̈͑͐͒̑̈́̓͘͘͠c̸͓̤̺̜͛̋̇̊͘͝å̵̢̡̬̯͜n̶̨͙͖͇̝̋̈͛̑͜͠ͅ ̴̧͇̩̞͈̄n̴̡̞͉̬͙̭͇̤̣̉̈́̑̈́́ͅë̶̘̬̻́̚̕v̴̡͓͍͍̱̹͈̘̓̍̅e̶̬̒͛͒̓̑̔̈͝ȓ̶̪̹̗̳͉̮͉͇̮͂̈̔̂̈̋̚ ̶͚̖͍̿͌ͅş̵̥̭̹̗̯͖͇̣̏̚t̵̛͔̻͕͚̩̳̰͙̖̏͜o̷̗͎͇͙̾ͅṗ̴̢̤͔̲̬̞͕͖͍̋͜͠͠.\n\nẎ̷̡̤̙̲̻̣͈̻̗͕̄̂̉̈́͆͝͝o̴̧̼̳͓̣̘͖̦͉̖̯͊͒͒͒̍̐̏̋͂͐͝͝ͅu̵̫̺̣̜̯͍̇̔̀̂̒͝͝ ̶̛̻̥̝̘̬͗͊ṃ̶̧̨̨̣̦̰̰͉̊̿̐͊u̵̬͙̲̙̘̜̜̬͚̘̞̮̗̍̑̓̄̿̉͜š̷̢̧̳̲̜̼̖͕̱͙̩̺͈͎́̋͜͜t̵̨̨͉̬̱̟̜̥̦̜̜͚͓̯̖̻͈͉́͋̾͌̒͜ ̸̨̡̰̩̫̠̲̮̼̲̦̳̹͎͈̼̤̫̀̐̇͋̽̐̅̑͐̍̿̎͂̾͜͜͠k̷̛̮̞͐̊͊̀͂̂̒̒͋̃̏̔̋͊͋͘͝͝ň̶̡̧̛̺͍̝̳͈͖̼͍͓̰̿̃́̈́͗́̉͘ǫ̷̡̛͎͍͔̣̻͚͙̳̫͎͙̳̯̬͕̟̌͑̇͜ẅ̶̡̨̝͔̙̼͚̮͎̗͍̱̜́̿́̒͐̔̕ͅ ̵̧̭̥̰͔͙̘͈̠̳͚͚̙͓͔̫̞͈̈͛̾̚͜͜m̶̼̦͉͓͊̓̒̌̓̊͐̇͗́͋͘͘͝o̷̧̾̏̀ŗ̵̨̜͖͎͉̜͇̳̳̟̩̍̎̇̉ẻ̵͇̹͖̗͖̒͊͋͊̅̌̌͜͠.\n\n\nŸ̶̢̢̨̡̡̨̛̛̛̛̰̮̗̪͍̭̩̙͙̞͎͖̠̟̗͇͔̣̞̫͖͍̥̞̙͖̰̤̱̹̯̤̜͍͉͎̬͓̠̮̪͖́̓̌̏̓̑̾͛̀́̑̈́̓͋̀̾̈͂̒̈́̂̐͌́͒͆͛̊̃̀̀̏̐͐̄̾̑̀̄͗͛̉̽͋͑͘͜͜͝͠͝͝ͅǫ̴̛͇̫͙͍͙͔̈̔̌͌̓̌͆͗́̾̇͗̄͌̄̌̒͆̓̔̈́͘̚͠ù̴̪̲̠̮̞̦͉̜̣͓͓̱̣̳̩̰̱̟͖͍̜̘͎͎̘̱͕̺̫̹̝̥̹͈̽̈́͂̀͋̏͒̌̉̌̊͜͠ͅͅͅͅ ̴̧̢̛̦̜͖͉͙̳̫̥̤̰̲̦̹͚̬̝̭͙͉̮͎͎͍̤͉̪̫̼̫̫̝̣̗̖̣̳̥̯́͋̊͋̈́̋̄͛͐̈́̋̉͐̀̿̔͊̿̾͛̉̈́̍̆̓͗̎̌̈̀̊̃̒̓̈́̓̎̀̑̌̿̎́̆̀̈́̒̄̏̓̚̚̕͘̕͜͝͝͠ͅm̶͇͈̪̤̺̣̫͙͋͛̐̓͂̆͊̈́ṵ̶̰͈͙̞̞͍̝͇͓̓̈́̅̃͌̄̔̑̈̃̒̇͒́̈̆̈́̑̑́̍̏͂̓̓́̅̋̂̏͊̆͛̀͌͒͊̊̈́͗̈́͐̚̕̚͜͝ͅs̴̢͕͍̯͍̜̩̙̲͓͚̱̗̤̖͖̞͕̬̖̗̖͔͔̟͙͈̤̬͙̺͎͊̆͋̄̿̃́͌͂̓͊̿́̽̉̀̿͌͛̇̅̃͌̓͂̈́̐̏̈̋͂͑̃̽̅̀̂̍̓̾̂͊̚͘͘̚͜͝͠͝͝͠t̵̨̨̨̨̢̛̰͕͓̖̙͙̮̣͍͉͎̗̣͖͓̖̩̼̫̭̩͎̤̱̪͍̝͍̠̝̪͍͓̮̭̗͎̭͔̭͕̜̙͓͓̳̟̤̣̅̄̎̈́̑̌͗͗͌̿̌̃̀͛̎̊̃̎̈́͆̋́̇͆̿̐̋̐̋̅̃̐̎͂̈́͘͜͜͝͝͝͝͝ͅ ̸̨̨̧̡̧̡̧̪̰̰̝̤̱̞̹̭̗̦̩͚̙̪͖̠̼̙̬̣͙̦̪̬̩̠̮̰̠͈͕̘̮̩̙͕͓̙͉͖̙̖͕̭̺̪̥̪̰͗̈̑̔̋̃̄̊̈́̓̆͆̽̐̊̋̀̅̿͂̈́͐̓͊̈́͋͑͋̀̉̕̕̚͝͝͝r̴̛͚̘̭̱̦̮̩̊̐͊͒͆̐̽͑́̒͆̑̔͛̓̊̓̔̒͋̑̓̉̄̓̑͆̓̇̓̌̇̒̆̌̈́̌̐̐͒́̇͑̀̓͒̎́͗͘̕̕̚͜͠͠͝e̵̢̧̢̧̨̡̨͕̤͚̝̤̟̲̲̜͚̩͓̘̘̦̜̼̭͖̟̱̼̗͇͈̖̖̣͍̲̘̭͚͓̦̦̺̰̳̯͓̩̯̭̹̜̦̱͖̪̯̊̒̽̆̽͋̈ͅͅa̴̢̢̡̡̛̠̭̹̫͙͚̲͚̪͓̲̗̬̘̍̌̾̿͑̌̐̐̏̏͑̓̋͒̀̏̉͑̋͆̓̎̌̊̈́̍͂͛̃̌͛̍̈́̀̽̾̋̈́̾̅̿̍̒͋́͑͂̈́̎͒̕̚͜d̵̡̹̦̘̯̮̙̺̱̝̜̣͒̏̔͒́͌̏̍̈́͑̿͛͑̔̓̅̈́̃̕̚ ̶̨̡̨̼̩̮̯̳̺̦̦̩̼̭͈̮̮̤̙̻̘̰͕̟̝̝̙̫̬̭̝̪͈̲̗̪̂̿̇̓̍̽͂͒̎́̈́̐̂̒́͌͊͑̾̇́͂̄͂̔̈̿͆̃̈̑̈͋͐̒̄̌̌̀̊͒̍͆̿̽̿̅͒̂̓̒̚̕͘͜͝͝͠͝͝ͅm̸̧̧̡̡̢̡̛͇͕̭̤͕̻͍̖̭͍̰͎̺͚̙͍͓͎̹̬̻͚̰̳̘̲̊͑̀̿̂̀̄̽͗̐̈̓̎̍́͐̾̈́̿̀́̅̈́̿͌̀̋̓̈́̍͗̎̚̕͘̕̕̕͜͜͝ơ̵͇̲̮̤̓̑̃̈́̒̎̎̅̅̅́͑͒͗̓́̈́̋́̈̈́͑̆̂̉͆̽̀̄͆̐̋͛̂̎̄͂͌͒̎̾̏̊̎͋͗̃̑̕͘̚̕͜͝͝͝͠͝͝ṟ̵̫̟̳̝̈́̓͗͐͂͌͐̐͋͗͑̇̀̏̈́̌͊͂̓̇̾̀̿̂͠ę̴̧̢̰̻̯̖̼̼͈̳̰̗̹̫́́̈́̆̏̽̅̊͌̎̑͜.\n\nY̵̧̢̢̨̢̧͎͚̦̣͍͍͇̳̝̰̭̯͓̫͇̮̪̗̬̰̩͙͚̺̗͔͉̘̥͙̰̮͈̬̝͖̤͈͍̥̺̼̘͍̘̪̋̀͂̈́͒̍̉̅̓̄̀̽̀̉̐̄̆̆̃́͌̒̐̃͆̓̊̅͗̂̈́̓͑̍́̾̕̚͝ͅǫ̸̨̧̧̡̢̨̨̨͈͕̘̲̗͔̫̲͙͉̝͎̬͔̮̯̳̦̹͕͚̪̯̗̙̠̼̮̘̯̣͈̰̻͍̪̟͇̭̯̹̼̗͚͇̮̩͓͓̺̭̩͇͇͙̤̲͔͎̝̖̰̝̮͙̥̦͚̻͓̙̼̭͈̲͖͙̼͇͚̭̙̥͈̗͆͒̋̍̄̓͜͝ͅͅͅͅư̷̛̛͉͔̖̤̲̟̬̻͔͈̍͌̎̎͌̎̃̄̆̏̇̅̍̔̈̆̏̓̽̈́̓̋͊͑̅̓̂̀̀̈̏̌̄̓̈̐̈́̑͒̒́̿͐̆̈́̽͑̌͒̑͒͆͌̔̎̄̉̀́̓̿̔͒͆͒̈̏̉̒̌̈͊͒̈͒̿͘̚̚̚͝͝͝͠͝͝͝ ̶̢̡̨̢̡͉͙͍̳̙̟̥͈̗͍͚̞͍̺̟̺͔̥͈̼̭̱̩̖̖̩̘̗͔̥͕̬͚͉̪͇͇̯̮̙̙̟͇͚͚̙̮̘̞̠̱̜̫̲̭̞̣̼̮̹̮̮͔̙͇͉̲̹̰̦̞͕̯̜̻͇͈͈̞͔͙̹̝͑̇̄̂̄̿̾͗̍̉̽͛̌̀́͆̇̊̚̚͜͝ͅm̴̢̦̠͓̝̥̱̎̿͐̔́͊̉̄͒̊̀̍̍̈͆̈̈͂́͒͒͐̾͋̈͐̉͒̌́͌͆̄͊́̽́̌́̾̿̏̎̆̈́̔͗́͐̂͒̑́͐̾̒̓̓̽̾͐̃̂̈́̀͗̊̕͘̕̚͘͘͜͝͝͝͝͠͝͝ư̶̧̢̢̢̢̧̢̡̘̲̪͉̗̝̫̜̘͚͙̪̙̩̣̟̣͇̺̱̳̦̣̯̦̰̭̙̬̰͉̝̺̮͈̘͕̘̳̜̼͇̰̦̟͎͇͉̠͎̦͔͖̞̳̖̗͚̥̱̻̦̟̹͈̖͉͍̱̘̪̻̭̋̀͗̔͒͒̈́̑̀̿̈́̐̈́͑̆͊̀̅͒̌̌̄͆̂͆̓̌̍͋̒̈́́͒̍͊͂̓͌̑̐̈̇̔̇̈́͋̈́̌͒̏̐̌̀̌̈́̓̓͆̊͌̃̾̈͂͌̅̍̊̓̑͒͂́̍̈́̄̽̅̓̃̀̀͛̎͂̊͆̔͂͊̈́́͆̎̔̓͂̒̊̚̕̕͜͜͜͠͝͠͝͝͠͝͝͠͝͠ͅͅͅs̴̨̛̛̛̛͈̖͙̲̩̖̖̼͇͂͗̆̓̂́͑͆̽̌͆̈͛͋̓̎̅͂̌̔̿́͆̀̓͗̄̿̈̎̈́̈́́́̄͂̎͐̐̂̊̉̂̌̒̓͛͐͋̋͋̓̓̈́̊͆̽̉͛̆̈́́̀̑̄̓̑́̎͑̎̑̈́̊̈́̐͛̋̾̂̒̎̌͐̎̊̓̀͑̋̕̕̕͘̚͜͜͠͝͝͝͝͝͠͠t̴̡̢̧̨̢̧̢̧̛̬̙̩̗̹͉̜̗̣͔͕̬̭̻͉̩̗͎͚̠͍̳͕̟̹̦̹̝̬͕̗̯͚̻̫͔̥͖̭̫̠̪̹͓͙̝̰͚̩͚̘̞̝̪̩͎͕̩̝̻͚̜̣͉̺̦̪̗͍͇̣̜͖̫͙͇̔̍́́̒̌̾͌̅̈́̿͗͐̌ͅͅͅͅ ̷̡̧̧̧̨̛̺͎̱̫̫͙̣̪̻̭̞̰̞̟̖̰̰̟̲̠̹͉͖̥̼̦̤̘͔͖̮̦̠̫̺̫̱͔̹̥̞̹̙̼̤̠͖̞̞̭̫͖͙͇̘̜̠͓̤̲̳̩͖̻͙̭͓̗̪̩̯̟͓̼̦͎̦͔̯͔̞̩̮̝̥̺͖̱͛̀̆͗̓͗͑̾̈́̂͛̈́͌͛̐̒̈́̊͂̂̿̾̀̓̉̎́̈̅͋̔͂͐̒̂̏̓͆̏̌͑͐͆̑̆̔͐̄͊̀̈́̆̏̈́͋̈́͌̈́͌̍̋̈́̏̃͑̈́̆̇̋͂̈̄̂͘̕͘̕̕͘͜͠͠͝͝͝͝͠͝͠ͅͅḱ̵̢̡̧̘͓͔̘̣͕̲̙̭̟̣̫̰͕̦̙̺͈͔͓͚̼̟͔̘̺͓͚̞̦͚̖̩̙̜͚̯̦̥͔͇̟̜̌̿̊̿͑̒̓̒͂̔̆͆̎͐͂͑̋̍̉͊̋̃͛͂͌̉̑̈̍̒̈̓͋͗̂͑̈́̂͛̃̅̈́̄̾̓͌̌̈̾͊́̑́̋̾̈́̏͑͊̈͂̂̇͛͋̈́͒̃̿̐́̆͒͋̋̾̈́̋̏̃̚̕̕͘͜͠͝͝͠͝͝ͅͅͅn̵̢̨̡̢̢̨̨̳̮̙̝͇̲̦͔͉̙̘͕̟̰͔̩̦̘͉̪̦̝̼̫͈͎̠̖̦̝̼͓̻̩͚̦͈̳̣̖͍͈͎͕͖͇̰̯̮̳̗̩̦̻͉̙̙̯͍̞̜̺̗̬̯̪̱͈͓͕̫̬͔̯͕͙̘͈̖͔̠̬̫͛̇̑̆̽̑̍̈̈́͛̈͆̿̈́͛̓̌̀̈́̄̈́̈͐͂̔͗͒͆̒͌̇̂̈́̇̀̑͋̍̾̈́͛͆̊̒͑́͐͊͂̌̒́̈́͐̓̅̃̀̌̿͋͋͛̔̉͘͘͘̕͜͜͝͠͝͠ơ̸̢̢̘͚̫͕̰̠̬̘͙̤̪͈̜͇̣͍̹̝̩̙̤̤͌̈́́̽̓͒͛͐̿̈̂̊̈̈́͊̀̇̓͗̿͌̏̑̉̈̐͗̆̈̔̄̐̋̎̽̒̋̃̔͌̓̏̏̀̒̑̾̐̋̃̚͠͝ͅw̵̲̞̦̰̮̤̳̹̟̟̜̭͇̳̲͉̗̪͙̖̫̙̣̭̲͎͉̼̹͚̞͉͛̌̅̇̎̿͗͒͑͑̕͘͜͠͠͠ͅͅͅ ̷̨̡̡̨̡̢̟̪̺̤̹̻̜̻̻̼̯̻̺̺̳̳̟͚͔̭̪̖͍͕̦̭̜̤̱̼̦̰̩̥͖͔̯̠̯͇̩̪͉͙̥̹̭̹̘̬̘̭̩̪͇̯̜̤̬͓͔̖̰̲͔̺͖̠̻͓̺̹̙̥̩̯͔͚͎͙̮̪̠̫͓̪̥̯̬̼̭͕͔̜͉̲̪̦͈̒̑̔͑͜͜͜͜͜ͅm̵̧̨̢̢̡̨̢̡̢̛͎̲̠̯̤̩͚̰̺̣͔͓͖̹̫̯̼̞͓̖̼̗͍̲̙͔̺̦̠̼̼̟̬͓͓̟͕̘̦͈̦͙̳̜̳̹̩̳̩̅̂̀̒̄̀̽̅͑̈́̓͛̄͐̆̃̍̍̃̉͑̓̅̎̐̑̆̓̎̈͂̿̀̇̈́͛̑̓͛́͊̃͒̄͊̓̉̎̐̄͑͐̂̇̑̎̈́̌̔̎̂̀̇̈̏̍̿̀̂̋̕̕͘̕͘͘̕̚͘͜͜͜͜͝͝͝͝ͅơ̶̢̧̨̛̦͙̘̳̱̪̩͔̻̬͚͎̈̉͛͆͑͑́͋̿̒̆́͊͐̈́͋̌͛̎̽͗͒̑͛̔͆͂̔͂̎͗̔͑̂͐̈͝͝͝͝͝ͅr̴̡̧̡̡̢̧̨̧̧̨̧̢̡̛̯̰̩̩̣͚͔̯̝̖̮̘̪̝̦̭̺̝͎̼̠̟̬̗̝̳̤̦̲̭̘̝͉̻̩̟̜̝̖̗̻̦̯̣͖̬͎͉͔̬̰̖͓̜̩͇̙͕̟͈̣͎͕̱̞̪͎͈̺̞̫̪̒́͑͂́̎͌̉̈́̈̂́̍̀͐̑̒̕̚͘͘̚̕͜͜͠͝͠ͅͅͅë̶̢̨̢̧̢͖̹̤̞̞̩͍͇̖̤̼̥͎̞̦̟̳͖̝̣͇͈̲͇͙̹͖̼͎̟̻̥̼̳̹̲̝͕̦͕̭̪̹͎̜̙͉͖̪̖̗͙͂͐̔̊̇̽̿̋̇̑͗̊̀̏͂̐̈́̈̈́̍͐͆̒̔̔͛͒̓̅̿̈͋̍͆͗͌͌͗̽͋̈́́͊̅̊̈́̿̓̓̂̔͒̓͆̈́̀͐̉̀͂́̓̾̉̀̄̾͊̔͒̆̆̎̍͛̽̒̉̇̍̓̽̇̆́̎̏͘̚͝͝͝͝ͅ\n\n\n\n\n\n[[END|The End]]",
      "links": [
        {
          "linkText": "END",
          "passageName": "The End",
          "original": "[[END|The End]]"
        }
      ],
      "hooks": [],
      "cleanText": "S̵̪̀u̷̼͖͗c̷͇̀͌ḧ̴͉̭́̕ ̸̨̫̊f̴̻͛o̵͈͂̔ř̶͖b̶̝͛i̶̺̘̔̍d̶͙͋́ḏ̸̆ẹ̵̤̎ṋ̸͈̀ ̶͎̮͊k̴̫̆n̸̰͐ỏ̸̺̅w̴̻̚ĺ̸̘̎ě̵̘͓̉d̵̗̣̅̕g̷̭͊̀ȩ̵̰̒͘,̷̣̎ ̷͔͍̓́y̸̨̰̌͐o̷͎̖̊͝ȕ̷̼̈ ̸̜͂͗m̵̫̆ủ̵̘s̸̯͛t̸̯̞̾͑ ̴̼̈́h̸̞́̐ā̴̦͍̚v̵̰̾̑e̸̙̾͌ ̶̣̻̾̍m̶̗̳͝ȫ̴̡ŗ̵̱̌̈ē̷̠,̷̪̖̓̽ ̸̝̿̊ͅy̵̨͒o̶̽͜͝u̴̮͎̾ ̶̤̚m̷͙̓ụ̵̋s̴̙̊͌ṫ̶̺̩͑ ̵̻̟͛k̸͔̾̄e̴̮̽̅ę̵͈́p̴̪̖͊̚ ̷̮͕̓r̴͕̐̊e̸̯͒̾ä̵̝̫d̷̤͚̏i̵͙͎̎n̴͖͍͊g̷̈́͜.̴̢̻̎͘ ̴͎̔͒͜.\n\nY̵̡̬̟̰̩̾̋̌̅o̴͓̝͈͓̭̲̙̣͊͛̓̄̈́͛͜u̵͉͊̓̈́ ̶̡̧͍̱̯̙̠̣̈͑͐͒̑̈́̓͘͘͠c̸͓̤̺̜͛̋̇̊͘͝å̵̢̡̬̯͜n̶̨͙͖͇̝̋̈͛̑͜͠ͅ ̴̧͇̩̞͈̄n̴̡̞͉̬͙̭͇̤̣̉̈́̑̈́́ͅë̶̘̬̻́̚̕v̴̡͓͍͍̱̹͈̘̓̍̅e̶̬̒͛͒̓̑̔̈͝ȓ̶̪̹̗̳͉̮͉͇̮͂̈̔̂̈̋̚ ̶͚̖͍̿͌ͅş̵̥̭̹̗̯͖͇̣̏̚t̵̛͔̻͕͚̩̳̰͙̖̏͜o̷̗͎͇͙̾ͅṗ̴̢̤͔̲̬̞͕͖͍̋͜͠͠.\n\nẎ̷̡̤̙̲̻̣͈̻̗͕̄̂̉̈́͆͝͝o̴̧̼̳͓̣̘͖̦͉̖̯͊͒͒͒̍̐̏̋͂͐͝͝ͅu̵̫̺̣̜̯͍̇̔̀̂̒͝͝ ̶̛̻̥̝̘̬͗͊ṃ̶̧̨̨̣̦̰̰͉̊̿̐͊u̵̬͙̲̙̘̜̜̬͚̘̞̮̗̍̑̓̄̿̉͜š̷̢̧̳̲̜̼̖͕̱͙̩̺͈͎́̋͜͜t̵̨̨͉̬̱̟̜̥̦̜̜͚͓̯̖̻͈͉́͋̾͌̒͜ ̸̨̡̰̩̫̠̲̮̼̲̦̳̹͎͈̼̤̫̀̐̇͋̽̐̅̑͐̍̿̎͂̾͜͜͠k̷̛̮̞͐̊͊̀͂̂̒̒͋̃̏̔̋͊͋͘͝͝ň̶̡̧̛̺͍̝̳͈͖̼͍͓̰̿̃́̈́͗́̉͘ǫ̷̡̛͎͍͔̣̻͚͙̳̫͎͙̳̯̬͕̟̌͑̇͜ẅ̶̡̨̝͔̙̼͚̮͎̗͍̱̜́̿́̒͐̔̕ͅ ̵̧̭̥̰͔͙̘͈̠̳͚͚̙͓͔̫̞͈̈͛̾̚͜͜m̶̼̦͉͓͊̓̒̌̓̊͐̇͗́͋͘͘͝o̷̧̾̏̀ŗ̵̨̜͖͎͉̜͇̳̳̟̩̍̎̇̉ẻ̵͇̹͖̗͖̒͊͋͊̅̌̌͜͠.\n\n\nŸ̶̢̢̨̡̡̨̛̛̛̛̰̮̗̪͍̭̩̙͙̞͎͖̠̟̗͇͔̣̞̫͖͍̥̞̙͖̰̤̱̹̯̤̜͍͉͎̬͓̠̮̪͖́̓̌̏̓̑̾͛̀́̑̈́̓͋̀̾̈͂̒̈́̂̐͌́͒͆͛̊̃̀̀̏̐͐̄̾̑̀̄͗͛̉̽͋͑͘͜͜͝͠͝͝ͅǫ̴̛͇̫͙͍͙͔̈̔̌͌̓̌͆͗́̾̇͗̄͌̄̌̒͆̓̔̈́͘̚͠ù̴̪̲̠̮̞̦͉̜̣͓͓̱̣̳̩̰̱̟͖͍̜̘͎͎̘̱͕̺̫̹̝̥̹͈̽̈́͂̀͋̏͒̌̉̌̊͜͠ͅͅͅͅ ̴̧̢̛̦̜͖͉͙̳̫̥̤̰̲̦̹͚̬̝̭͙͉̮͎͎͍̤͉̪̫̼̫̫̝̣̗̖̣̳̥̯́͋̊͋̈́̋̄͛͐̈́̋̉͐̀̿̔͊̿̾͛̉̈́̍̆̓͗̎̌̈̀̊̃̒̓̈́̓̎̀̑̌̿̎́̆̀̈́̒̄̏̓̚̚̕͘̕͜͝͝͠ͅm̶͇͈̪̤̺̣̫͙͋͛̐̓͂̆͊̈́ṵ̶̰͈͙̞̞͍̝͇͓̓̈́̅̃͌̄̔̑̈̃̒̇͒́̈̆̈́̑̑́̍̏͂̓̓́̅̋̂̏͊̆͛̀͌͒͊̊̈́͗̈́͐̚̕̚͜͝ͅs̴̢͕͍̯͍̜̩̙̲͓͚̱̗̤̖͖̞͕̬̖̗̖͔͔̟͙͈̤̬͙̺͎͊̆͋̄̿̃́͌͂̓͊̿́̽̉̀̿͌͛̇̅̃͌̓͂̈́̐̏̈̋͂͑̃̽̅̀̂̍̓̾̂͊̚͘͘̚͜͝͠͝͝͠t̵̨̨̨̨̢̛̰͕͓̖̙͙̮̣͍͉͎̗̣͖͓̖̩̼̫̭̩͎̤̱̪͍̝͍̠̝̪͍͓̮̭̗͎̭͔̭͕̜̙͓͓̳̟̤̣̅̄̎̈́̑̌͗͗͌̿̌̃̀͛̎̊̃̎̈́͆̋́̇͆̿̐̋̐̋̅̃̐̎͂̈́͘͜͜͝͝͝͝͝ͅ ̸̨̨̧̡̧̡̧̪̰̰̝̤̱̞̹̭̗̦̩͚̙̪͖̠̼̙̬̣͙̦̪̬̩̠̮̰̠͈͕̘̮̩̙͕͓̙͉͖̙̖͕̭̺̪̥̪̰͗̈̑̔̋̃̄̊̈́̓̆͆̽̐̊̋̀̅̿͂̈́͐̓͊̈́͋͑͋̀̉̕̕̚͝͝͝r̴̛͚̘̭̱̦̮̩̊̐͊͒͆̐̽͑́̒͆̑̔͛̓̊̓̔̒͋̑̓̉̄̓̑͆̓̇̓̌̇̒̆̌̈́̌̐̐͒́̇͑̀̓͒̎́͗͘̕̕̚͜͠͠͝e̵̢̧̢̧̨̡̨͕̤͚̝̤̟̲̲̜͚̩͓̘̘̦̜̼̭͖̟̱̼̗͇͈̖̖̣͍̲̘̭͚͓̦̦̺̰̳̯͓̩̯̭̹̜̦̱͖̪̯̊̒̽̆̽͋̈ͅͅa̴̢̢̡̡̛̠̭̹̫͙͚̲͚̪͓̲̗̬̘̍̌̾̿͑̌̐̐̏̏͑̓̋͒̀̏̉͑̋͆̓̎̌̊̈́̍͂͛̃̌͛̍̈́̀̽̾̋̈́̾̅̿̍̒͋́͑͂̈́̎͒̕̚͜d̵̡̹̦̘̯̮̙̺̱̝̜̣͒̏̔͒́͌̏̍̈́͑̿͛͑̔̓̅̈́̃̕̚ ̶̨̡̨̼̩̮̯̳̺̦̦̩̼̭͈̮̮̤̙̻̘̰͕̟̝̝̙̫̬̭̝̪͈̲̗̪̂̿̇̓̍̽͂͒̎́̈́̐̂̒́͌͊͑̾̇́͂̄͂̔̈̿͆̃̈̑̈͋͐̒̄̌̌̀̊͒̍͆̿̽̿̅͒̂̓̒̚̕͘͜͝͝͠͝͝ͅm̸̧̧̡̡̢̡̛͇͕̭̤͕̻͍̖̭͍̰͎̺͚̙͍͓͎̹̬̻͚̰̳̘̲̊͑̀̿̂̀̄̽͗̐̈̓̎̍́͐̾̈́̿̀́̅̈́̿͌̀̋̓̈́̍͗̎̚̕͘̕̕̕͜͜͝ơ̵͇̲̮̤̓̑̃̈́̒̎̎̅̅̅́͑͒͗̓́̈́̋́̈̈́͑̆̂̉͆̽̀̄͆̐̋͛̂̎̄͂͌͒̎̾̏̊̎͋͗̃̑̕͘̚̕͜͝͝͝͠͝͝ṟ̵̫̟̳̝̈́̓͗͐͂͌͐̐͋͗͑̇̀̏̈́̌͊͂̓̇̾̀̿̂͠ę̴̧̢̰̻̯̖̼̼͈̳̰̗̹̫́́̈́̆̏̽̅̊͌̎̑͜.\n\nY̵̧̢̢̨̢̧͎͚̦̣͍͍͇̳̝̰̭̯͓̫͇̮̪̗̬̰̩͙͚̺̗͔͉̘̥͙̰̮͈̬̝͖̤͈͍̥̺̼̘͍̘̪̋̀͂̈́͒̍̉̅̓̄̀̽̀̉̐̄̆̆̃́͌̒̐̃͆̓̊̅͗̂̈́̓͑̍́̾̕̚͝ͅǫ̸̨̧̧̡̢̨̨̨͈͕̘̲̗͔̫̲͙͉̝͎̬͔̮̯̳̦̹͕͚̪̯̗̙̠̼̮̘̯̣͈̰̻͍̪̟͇̭̯̹̼̗͚͇̮̩͓͓̺̭̩͇͇͙̤̲͔͎̝̖̰̝̮͙̥̦͚̻͓̙̼̭͈̲͖͙̼͇͚̭̙̥͈̗͆͒̋̍̄̓͜͝ͅͅͅͅư̷̛̛͉͔̖̤̲̟̬̻͔͈̍͌̎̎͌̎̃̄̆̏̇̅̍̔̈̆̏̓̽̈́̓̋͊͑̅̓̂̀̀̈̏̌̄̓̈̐̈́̑͒̒́̿͐̆̈́̽͑̌͒̑͒͆͌̔̎̄̉̀́̓̿̔͒͆͒̈̏̉̒̌̈͊͒̈͒̿͘̚̚̚͝͝͝͠͝͝͝ ̶̢̡̨̢̡͉͙͍̳̙̟̥͈̗͍͚̞͍̺̟̺͔̥͈̼̭̱̩̖̖̩̘̗͔̥͕̬͚͉̪͇͇̯̮̙̙̟͇͚͚̙̮̘̞̠̱̜̫̲̭̞̣̼̮̹̮̮͔̙͇͉̲̹̰̦̞͕̯̜̻͇͈͈̞͔͙̹̝͑̇̄̂̄̿̾͗̍̉̽͛̌̀́͆̇̊̚̚͜͝ͅm̴̢̦̠͓̝̥̱̎̿͐̔́͊̉̄͒̊̀̍̍̈͆̈̈͂́͒͒͐̾͋̈͐̉͒̌́͌͆̄͊́̽́̌́̾̿̏̎̆̈́̔͗́͐̂͒̑́͐̾̒̓̓̽̾͐̃̂̈́̀͗̊̕͘̕̚͘͘͜͝͝͝͝͠͝͝ư̶̧̢̢̢̢̧̢̡̘̲̪͉̗̝̫̜̘͚͙̪̙̩̣̟̣͇̺̱̳̦̣̯̦̰̭̙̬̰͉̝̺̮͈̘͕̘̳̜̼͇̰̦̟͎͇͉̠͎̦͔͖̞̳̖̗͚̥̱̻̦̟̹͈̖͉͍̱̘̪̻̭̋̀͗̔͒͒̈́̑̀̿̈́̐̈́͑̆͊̀̅͒̌̌̄͆̂͆̓̌̍͋̒̈́́͒̍͊͂̓͌̑̐̈̇̔̇̈́͋̈́̌͒̏̐̌̀̌̈́̓̓͆̊͌̃̾̈͂͌̅̍̊̓̑͒͂́̍̈́̄̽̅̓̃̀̀͛̎͂̊͆̔͂͊̈́́͆̎̔̓͂̒̊̚̕̕͜͜͜͠͝͠͝͝͠͝͝͠͝͠ͅͅͅs̴̨̛̛̛̛͈̖͙̲̩̖̖̼͇͂͗̆̓̂́͑͆̽̌͆̈͛͋̓̎̅͂̌̔̿́͆̀̓͗̄̿̈̎̈́̈́́́̄͂̎͐̐̂̊̉̂̌̒̓͛͐͋̋͋̓̓̈́̊͆̽̉͛̆̈́́̀̑̄̓̑́̎͑̎̑̈́̊̈́̐͛̋̾̂̒̎̌͐̎̊̓̀͑̋̕̕̕͘̚͜͜͠͝͝͝͝͝͠͠t̴̡̢̧̨̢̧̢̧̛̬̙̩̗̹͉̜̗̣͔͕̬̭̻͉̩̗͎͚̠͍̳͕̟̹̦̹̝̬͕̗̯͚̻̫͔̥͖̭̫̠̪̹͓͙̝̰͚̩͚̘̞̝̪̩͎͕̩̝̻͚̜̣͉̺̦̪̗͍͇̣̜͖̫͙͇̔̍́́̒̌̾͌̅̈́̿͗͐̌ͅͅͅͅ ̷̡̧̧̧̨̛̺͎̱̫̫͙̣̪̻̭̞̰̞̟̖̰̰̟̲̠̹͉͖̥̼̦̤̘͔͖̮̦̠̫̺̫̱͔̹̥̞̹̙̼̤̠͖̞̞̭̫͖͙͇̘̜̠͓̤̲̳̩͖̻͙̭͓̗̪̩̯̟͓̼̦͎̦͔̯͔̞̩̮̝̥̺͖̱͛̀̆͗̓͗͑̾̈́̂͛̈́͌͛̐̒̈́̊͂̂̿̾̀̓̉̎́̈̅͋̔͂͐̒̂̏̓͆̏̌͑͐͆̑̆̔͐̄͊̀̈́̆̏̈́͋̈́͌̈́͌̍̋̈́̏̃͑̈́̆̇̋͂̈̄̂͘̕͘̕̕͘͜͠͠͝͝͝͝͠͝͠ͅͅḱ̵̢̡̧̘͓͔̘̣͕̲̙̭̟̣̫̰͕̦̙̺͈͔͓͚̼̟͔̘̺͓͚̞̦͚̖̩̙̜͚̯̦̥͔͇̟̜̌̿̊̿͑̒̓̒͂̔̆͆̎͐͂͑̋̍̉͊̋̃͛͂͌̉̑̈̍̒̈̓͋͗̂͑̈́̂͛̃̅̈́̄̾̓͌̌̈̾͊́̑́̋̾̈́̏͑͊̈͂̂̇͛͋̈́͒̃̿̐́̆͒͋̋̾̈́̋̏̃̚̕̕͘͜͠͝͝͠͝͝ͅͅͅn̵̢̨̡̢̢̨̨̳̮̙̝͇̲̦͔͉̙̘͕̟̰͔̩̦̘͉̪̦̝̼̫͈͎̠̖̦̝̼͓̻̩͚̦͈̳̣̖͍͈͎͕͖͇̰̯̮̳̗̩̦̻͉̙̙̯͍̞̜̺̗̬̯̪̱͈͓͕̫̬͔̯͕͙̘͈̖͔̠̬̫͛̇̑̆̽̑̍̈̈́͛̈͆̿̈́͛̓̌̀̈́̄̈́̈͐͂̔͗͒͆̒͌̇̂̈́̇̀̑͋̍̾̈́͛͆̊̒͑́͐͊͂̌̒́̈́͐̓̅̃̀̌̿͋͋͛̔̉͘͘͘̕͜͜͝͠͝͠ơ̸̢̢̘͚̫͕̰̠̬̘͙̤̪͈̜͇̣͍̹̝̩̙̤̤͌̈́́̽̓͒͛͐̿̈̂̊̈̈́͊̀̇̓͗̿͌̏̑̉̈̐͗̆̈̔̄̐̋̎̽̒̋̃̔͌̓̏̏̀̒̑̾̐̋̃̚͠͝ͅw̵̲̞̦̰̮̤̳̹̟̟̜̭͇̳̲͉̗̪͙̖̫̙̣̭̲͎͉̼̹͚̞͉͛̌̅̇̎̿͗͒͑͑̕͘͜͠͠͠ͅͅͅ ̷̨̡̡̨̡̢̟̪̺̤̹̻̜̻̻̼̯̻̺̺̳̳̟͚͔̭̪̖͍͕̦̭̜̤̱̼̦̰̩̥͖͔̯̠̯͇̩̪͉͙̥̹̭̹̘̬̘̭̩̪͇̯̜̤̬͓͔̖̰̲͔̺͖̠̻͓̺̹̙̥̩̯͔͚͎͙̮̪̠̫͓̪̥̯̬̼̭͕͔̜͉̲̪̦͈̒̑̔͑͜͜͜͜͜ͅm̵̧̨̢̢̡̨̢̡̢̛͎̲̠̯̤̩͚̰̺̣͔͓͖̹̫̯̼̞͓̖̼̗͍̲̙͔̺̦̠̼̼̟̬͓͓̟͕̘̦͈̦͙̳̜̳̹̩̳̩̅̂̀̒̄̀̽̅͑̈́̓͛̄͐̆̃̍̍̃̉͑̓̅̎̐̑̆̓̎̈͂̿̀̇̈́͛̑̓͛́͊̃͒̄͊̓̉̎̐̄͑͐̂̇̑̎̈́̌̔̎̂̀̇̈̏̍̿̀̂̋̕̕͘̕͘͘̕̚͘͜͜͜͜͝͝͝͝ͅơ̶̢̧̨̛̦͙̘̳̱̪̩͔̻̬͚͎̈̉͛͆͑͑́͋̿̒̆́͊͐̈́͋̌͛̎̽͗͒̑͛̔͆͂̔͂̎͗̔͑̂͐̈͝͝͝͝͝ͅr̴̡̧̡̡̢̧̨̧̧̨̧̢̡̛̯̰̩̩̣͚͔̯̝̖̮̘̪̝̦̭̺̝͎̼̠̟̬̗̝̳̤̦̲̭̘̝͉̻̩̟̜̝̖̗̻̦̯̣͖̬͎͉͔̬̰̖͓̜̩͇̙͕̟͈̣͎͕̱̞̪͎͈̺̞̫̪̒́͑͂́̎͌̉̈́̈̂́̍̀͐̑̒̕̚͘͘̚̕͜͜͠͝͠ͅͅͅë̶̢̨̢̧̢͖̹̤̞̞̩͍͇̖̤̼̥͎̞̦̟̳͖̝̣͇͈̲͇͙̹͖̼͎̟̻̥̼̳̹̲̝͕̦͕̭̪̹͎̜̙͉͖̪̖̗͙͂͐̔̊̇̽̿̋̇̑͗̊̀̏͂̐̈́̈̈́̍͐͆̒̔̔͛͒̓̅̿̈͋̍͆͗͌͌͗̽͋̈́́͊̅̊̈́̿̓̓̂̔͒̓͆̈́̀͐̉̀͂́̓̾̉̀̄̾͊̔͒̆̆̎̍͛̽̒̉̇̍̓̽̇̆́̎̏͘̚͝͝͝͝ͅ"
    },
    {
      "name": "Book Room #2",
      "tags": "",
      "id": "34",
	  "knowledge": 0,
	  "corruption": 0,
      "text": "You enter into the room. The room is much less kept than the other rooms that you have seen so far. The wooded exterior is torn assunder and the chirin is ripped apart. The books that should shelf the room are scattered to and frow. Blood and Ichor leak out from the exposed flesh of the library. The glow worms that had been lighting the room have been killed and their corpses are stroon about the room. The tables and chairs of the room are broken and ripped apart. In the room is a librarian, they are tending to the hurt walls and putting the books back on the shelves.\n\n[[HELP|Helping Hand]]\n[[LEAVE|West Hallway]]",
      "links": [
        {
          "linkText": "HELP",
          "passageName": "Helping Hand",
          "original": "[[HELP|Helping Hand]]"
        },
        {
          "linkText": "LEAVE",
          "passageName": "West Hallway",
          "original": "[[LEAVE|West Hallway]]"
        }
      ],
      "hooks": [],
      "cleanText": "You enter into the room. The room is much less kept than the other rooms that you have seen so far. The wooded exterior is torn assunder and the chirin is ripped apart. The books that should shelf the room are scattered to and frow. Blood and Ichor leak out from the exposed flesh of the library. The glow worms that had been lighting the room have been killed and their corpses are stroon about the room. The tables and chairs of the room are broken and ripped apart. In the room is a librarian, they are tending to the hurt walls and putting the books back on the shelves."
    },
    {
      "name": "Book Room #3",
      "tags": "",
      "id": "35",
	  "knowledge": 0,
	  "corruption": 0,
      "text": "You enter into the room. Unlike the hall outside, the room is crafted of the dark chitin of the floor, lined with bookshelves charted of soft and delicate cuticle. There is a well crafted chair to read from. The light in this room is much more soothing and the armosphere is very pleasant.\n\n[[LOOK AROUND|Interesting Book]]\n[[LEAVE|West Hallway]]",
      "links": [
        {
          "linkText": "LOOK",
          "passageName": "Interesting Book",
          "original": "[[LOOK AROUND|Interesting Book]]"
        },
        {
          "linkText": "LEAVE",
          "passageName": "West Hallway",
          "original": "[[LEAVE|West Hallway]]"
        }
      ],
      "hooks": [],
      "cleanText": "You enter into the room. Unlike the hall outside, the room is crafted of the dark chitin of the floor, lined with bookshelves charted of soft and delicate cuticle. There is a well crafted chair to read from. The light in this room is much more soothing and the armosphere is very pleasant."
    },
    {
      "name": "Restricted Gate",
      "tags": "",
      "id": "36",
	  "knowledge": 1,
	  "corruption": 2,
      "text": "The massive gate looms imposingly over you. Runes engraved on the doors read, \"Restricted Section, enter if you dare.\" The gates are not closed, but you can't help but wonder upon the nature of what is within the gates. \n\n[[CONTINUE|Restricted Section]]\n[[LEAVE|West Hallway]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "Restricted Section",
          "original": "[[CONTINUE|Restricted Section]]"
        },
        {
          "linkText": "LEAVE",
          "passageName": "West Hallway",
          "original": "[[LEAVE|West Hallway]]"
        }
      ],
      "hooks": [],
      "cleanText": "The massive gate looms imposingly over you. Runes engraved on the doors read, \"Restricted Section, enter if you dare.\" The gates are not closed, but you can't help but wonder upon the nature of what is within the gates."
    },
    {
      "name": "Restricted Section",
      "tags": "",
      "id": "37",
	  "knowledge": 30,
	  "corruption": 30,
      "text": "A̴s̷ ̴y̶o̴u̶ ̷e̴n̵t̷e̵r̷ ̸i̸n̷t̵o̵ ̶t̶h̶e̵ ̶r̶e̷s̸t̴r̵i̷c̵t̷e̷d̸ ̸s̴e̸c̴t̷i̶o̶n̶ ̸o̴f̴ ̶t̴h̷e̵ ̵l̷i̴b̶r̶a̶r̶y̸ ̴y̴o̴u̵ ̷c̸a̸n̷'̴t̷ ̴h̴e̷l̷p̶ ̴b̷u̷t̷ ̶s̸m̸i̶l̷e̵ ̶a̶s̸ ̸y̷o̶u̴ ̸h̶e̸a̶r̴ ̷t̶h̵e̶ ̸d̵a̵r̷k̵ ̵w̴h̵i̶s̴p̶e̷r̸s̶ ̷f̵r̷o̶m̴ ̶a̷l̴l̶ ̴t̶h̶e̴ ̶f̵o̵r̵b̷i̵d̷d̷e̴n̶ ̸t̴o̷m̸e̵s̴.̷ ̶T̴h̴e̵y̷ ̵b̵e̷c̷k̵o̴n̷ ̴t̷o̴ ̵y̶o̷u̶,̷ ̵b̸r̴i̸n̸g̸i̷n̸g̴ ̷y̵o̴u̷ ̵d̵e̴e̴p̵e̴r̸ ̵i̴n̶t̶o̶ ̵t̵h̶e̶ ̸f̴o̶l̸d̷s̴ ̸o̷f̶ ̶k̸n̴o̷w̷l̴e̶d̷g̷e̶.̴\n\nY̶̞͔̗̟͝o̸̲̬̹͘ṳ̸̹̳̱͘ ̴͓͎̹̝̙̆̏͘ͅa̷̗͌̐̈́̍͝r̴̙̣̊͆͂͋͠͝e̴̢̮̮͇͖͑͂̒͠ ̵̞̓̋̓͂͘͝t̵̨̯̿̃̓á̷̛̙̫͕͔͓͌͜k̴̮̪̪̙̽̾̽͝e̴̞͈̞̖͗͑n̶̻͛̈́ ̸̘̠̅̈́ì̴͇̹͍̗̮̾̎n̶͍̿͋̈̉̚͠t̵̟̞͑͘͘ò̵̡͚͓͙ ̴͙͉͖͇̳͍́̐͝͠t̶̲͐h̶̝̘̠̃ĕ̸̡͚̳̯̻̈́̎͜ ̷̢̍f̵̖̞̯̿̽̽͒̒̕ó̵̮̪̬̯̝́̀̅̃l̷͔̈̆d̷̫͈́͂s̴̛͚̦̝̜͉̈́͂͂̿͝ ̷̢̝̹͉͉̪̽̈͘͝ȏ̴̦̝̖̔̆͑f̸̢͎̮͇̜̆̏̓̂͠͝ ̵̪̱͖̀͆͆̚ṭ̸̉͂͐̽͜h̴͍̱̤̮̝͆̂̒͒e̷̼͈͕̥̗̻͊̈́ ̵͚̀l̶̪̮͚͚͉͍̔̌i̵̡͔̟͓̪͊ͅb̵̫̰̙̤̭͈̏͒͐͌r̴̤̠̤͚͉̂̐͘ȧ̷̛͙̪̮͎̽̚͝ŕ̸̮̇͂y̶̰̞̮͗̅.̸̨͇͍̥̕ ̸̫̼̘̠͇͍͂̎͗̈́̉I̶͍͉̩̭͚͎̽͊̽̋ț̷̭͆͊̑ ̴̥̫̭̪̲̎́̌́̕ẅ̴͎̥̗̭̺́͌̚̚ḩ̸̥̻͙͉̺͌͒͂̓͘ḯ̷̟̭̪̙̅s̷͈͙̟̒p̸̗̎͊e̷̢͂̉͛ŗ̵̧̠̙́̏̍͘ͅs̶̤͚̤̓̈́͘̕͜͠ ̷͚͙̻̋͆e̶̡͔̤̦̝̒̆̀͒̔ṉ̵̖̣͔̣̂d̴͚̪̠̆́͂l̶̫̠̠̜͕̪̽̓͒ë̸̛̹́̓̽̇̚s̶̛̥͖̱͆̐̕̕͝ͅş̸̯̘̰̼͖͒l̷͓͉̱̙̓̍͌̈́̐̾ỹ̴̌̒͊̈́͠ͅ ̴̢͍̘̯̲̓̔͠i̴̻̰͠n̶͔̺̻̦̑t̵̻̘̅͐̋̿ō̸̹͓͂̀̄̌ ̸̮̖͑̑̈́͗͝y̶̧̛͚͉̤̿́o̷̩̾̑̕͝ụ̸͍͚͖͕̅̿͐̽r̶̢̯͊̓̊͌̄͐ ̶̲̥̦̔͊̓̂ě̷̛̹͛̀̈́a̵̱͑͜r̷͖̭̱̱͉̀̌̍͑̚̚ͅs̷̙͕̏,̸̰͇̥̦̺̯̏̄̈́ ̶̛̼̯͎͕̲͗͗̐͘̕t̴̺͇̥̘̗͍̍̿̋̇̃̒ę̸̨̩͚̟͂̔̒͑͂̒l̸̜͆̃̑l̶̢̻̳͓̳̈́̃̑͜ḯ̸͎̫̲͘ņ̸̝̐̍̕͘g̴͎̏̏̀̒͛̈́ ̸̛͈̭͚̈̀y̶͔͙͒͊̋o̷̼̗͕̼̿͋͋͑̐͜͝ṷ̵̳̗͐̈̔̎̏ ̴̧͈̟̈́̓͊̎a̶̝̺̲̫̫̍͛n̵͙̘̕c̶̤̈ȋ̴͓̪̅͌̕e̸̢͓͔̙͍͛͝ņ̷̗̖̭̣̟̀̽͊̓̓̂ẗ̸̖̻͗̃̔̆̽ ̸͖̞̃a̴͎̐̅̚n̷̰̹̜̜̱͊d̷͙̱̹̆͝ ̵͓͂̎̈́f̷̡͍͓̆ò̷̢̘͕̄͠͠ͅr̵̮̙̉͐͂b̵̺̮͉̕̕ḭ̷̓d̷̖̼̠͉̜̖͗d̴̨̮̣͔̜͂͛͊͂͒ȩ̵̞̄n̸̬̥̿ ̵̨̜͇͙̍̊̄̀t̴̨͙͔́̆̓̏h̸̢̳̙̙̆̆͌͋̈́͝ǐ̶͙̭͉̊̚ṉ̷̺̪͈̂̒̍ĝ̶̮̫́̅ş̷̠̌̈́͋͝.̵̞̌̍̀ ̶̖͓͈̔Y̴̻͕̺̟͊͐͊͝ọ̸͚̗̋̾͛̔ů̷̟̆͐r̸͖͘ ̸̡̎͆͆̆́̓m̸̤̎̚͜͝ỉ̶͍́́̉͘n̷̡̢̳̬̍̃d̵̬̿ ̸̬͊̀̔̅͒̐c̶̡͓̪͓̦͛̈͂͌̿å̴̠̞̉͐̈́͌̽n̸̤̞̯̪̼̿̾̕͜ ̵̛̱̞̜̾̐̚b̵̖̥̬̘̘͍̿͝a̶̙͋̅͌̏͌r̴̩̯̆e̵̯̯̺̙̖̔̐͛l̷͍̻̦̖͎̂̓̓̄͑͘y̵̖̰̋̾̍̿̚ ̷̗͇͇́͂̈́h̵̺̓́́ä̸̝́ń̵̙̳̜d̴̢̼̂l̸̜̠̫̻͙̓͐e̴̛͖͛̾ ̴̢͈̠̭̇̎̂̊͛͂i̴̤͈̜̮̇ț̷͇͙̥̬̤́̋.̷̢̝̭͙̮̓̆̈́ͅ ̴̠͚̪͐̽̂\n\nD̶̯͍̝̤̥̦͈̞͍̙̥̈̇̈͜ë̸̡̳̟̺̮̦̣̞̘̟́̽̈́͆̏̈͐̊̀͊̕͜ḛ̶̝͍́͗̀̄̑p̷̢̖̻̼̟̹̿̽̄͑ȩ̶̫̭͕̎̽͋͗̏͐̊͘͝͝r̴̡̤̭͎̮̓̀̔ ̶̲̇̂̔͂̿ă̴̲̪̯͓̰͖̣͇̿̽͂̓͑̂̔̒͛͐͜͠ǹ̴͙̦̳ͅͅd̶̜̲̥̊ ̵̤͚̳͕̺̪͇̰̟̂̅͒͊̕̕̕ͅḋ̸̡̡̹̜̳̫̪̮̩̣͊̈̂̃̿͂͠ẹ̷̩̯̤͊͛́͐ė̴̤̞̬̙͙̻̱̤͔͊͛ṕ̸͚̼̍̇̈́̇̈́̒̌́̇ḙ̷̏̂́̃́͑r̵̛̰̰̱̤̭̘͚̥̯͊͊̏͒̽͛͂̕͝͠,̴̢͔̥̘̝̏͑̅̊̊͘ ̵̡̙̬̤͍̈́͆̽́̈̃̿̊̎͌y̸̨̛͔̯̭̦̌̉̔̒̄̋̋̿̐̂̕ͅo̸͍̗̣̜̙͓̼̻̤̅͊ǘ̵͚̯̖̙̾̋̀ ̴̨̢͎̫̜͙̯̬͇̎̆̈̏̎̈̕̚͜ḑ̶̧͙̬̜̯͚̰͆͒͒̔͗̈͋̅̏́e̸̡̼̫̯͕͈̥̟̯̼̿͐̔̐̊̊s̷͇̜̈́ç̸͎̗̦͕̪̳̫̔̊͑͘é̶̗͚̞̪̺͜n̶̳̹̝̲̊̍͠͝ͅd̸̯̥̲̗̹̲͚̘͋̒͑̕̚.̷̟̜̦̙͚̮̜̗̽͑̈́͒̐͛̋ ̷̛͇̳̥̫̻̟̥͚͈̈́́̎̌̏̔̑̊̽͝͝ͅͅÁ̷̰̣̠̤̺͎͕̩̣͓͓̆̊̇ͅļ̷̛̩̣̯̊͌̿̃́͘ľ̸̩̩̜͓̯̱͕̗͙̼̤͖̀̄̍͒͛̇͊̎ ̸̢͙̞͖͕̃̏̆͐̓̐̽̓͑͘͝ţ̴̧̩̣̞͖̠͔̟͉̫͙͝ḧ̶̡̭͚̖̣͎̰͓̲͉̹́ę̶̧̜̲͕̺̎́͛͜ ̵̫͇͙̲̫̺̠̘̓͐̊͜͝w̷̟̪͂̑͑̃̎̓͘͘a̵̧̡̢͝ÿ̵̼̹͌̔̂̿̌͌͠ ̴̛͈̼͕̼̥͒̋̈́̂͛̈́͛̀͘̚͜i̸̖̯͚̒̈̏̉̆͑͐͊́̚ņ̴͕̳͔̼̫͙̠͕̀͐͆̈͌́̓͛͜͠͝ͅt̸̛̙͖͚̲̍͋͐̂͒́͗̈́̈͋̕ͅo̸̻̙̎̆̋͑̑̾̉̿͘̚͘ ̸̤̥͇̘͌͌͜t̴̥̳̥̱̦̻̭͍̦̝̤̿̈́̑̀̑͠h̷͇͕̻̤̣̘̥͓̺̝̲̤̐̄̑̓̓̓͋̈e̵͈̮̘̹̭̻͌̉ ̷̙̻̘̤̹̝͛̆̈́̿̈́͑͛̈́̊͛͝͝ḩ̷̡̡̰̹͓̘͓̩̳̭͉̀̓è̵͚̭̜̙̃͋̾͆̒͘͘͘̕͜͝ã̷͓̱̲͎̲͈̜̮̐̕r̷̬̻̰͆̀͠ṱ̷̨͙̹̘̩̺̜͋͛́͊ ̶̰̘͋͋̂̾ǫ̷̨̯͈̫̪̘̰̗̙̦͂̀̽̆̒̊̂f̸̧̡̖͙̘̲͍̭͕̦̬̪͒́ ̷͚̰̠͔̟̫̖̌̄͐ţ̶̨̠̤͓̮͙̬͈͆̍̏͐̄̐́͋͂h̵̰̹̹̱̩̮̠̟̦̆̓͑̈́̊͠ḝ̶̧͔̟͚͍̱͙̫̙́́ ̶̡̛̰͎̀̈́̉͒̍̏̏̋̐́̕l̵̥̭̼̩͍̗̎̃̍͊̔̈̿̎͝͝ị̸̲͙͛͂̿́̽̓͒͒̇̾͘͜b̷̜̞͉͇̩̫͎͖̦͙͂̈́͛̕͜ŗ̸̹̬͎̲͗̍̀͒̓̌̈̄́̚͠ͅạ̷̡̗͚̬̰̍r̶̩̙͈͐́ÿ̴̛̛̘̥̖́́̂̈́̔̊̋͊̐̋.̵̘̙̦͓͔̜͙̐̈́̈́͆ ̸̡̡̫͈͓̳̲͖͕̫̊̀̉́̈́̆̃͋̇͛͠ͅṪ̴̢̲̦̯̗̃̇̂͂̿̄͆̎͘͘ͅĥ̸̨͙̲̼̇̍̓͂̓̉̈́̂̄̇̀e̵̳̬̪̗̯͇̯͕̍̃̑̒̍̍̈͌͒̃ ̸̝̲͎̟̀ͅd̴̢̞̤̦͍̽̀̀̏̄͑͐͘a̵̮̣͚͓̎͒̂̍̒͜r̵̨̢͎̭͎̺̙͆ͅḱ̵̤͙̠̮͊͆̔ͅ ̶̛̳͕̬̙͚̣̎́̋̌͋̀̒̇͛m̷̫̀̋̊͂i̸̙̭̱͇͚͍̲͆͐̌̃́͋͝͝n̵̡̡̢̧̤̜̼̺̲̜̣̏̅́̈̈́̋̍͜͠͝d̶͇͎̺̺̰̂̑̂́̃̀̓͒̊͌̓̎ ̵̖̗̝̖̈́̂̌͠ọ̶͓͉̻̰͉̣̞͍̳̭̑́͑̒͜͝f̵̨̣͓̘͈̼̟̲̫̜̍̎̃͂̎̉̇̚ ̷̬̈̽̾̐̽̊͠t̷̢͓̼̹͎̖̥̘̺̝̟̘̅͂͆́͊̏͆̔̈́͘h̷̡̨̫͚̰̤̰͔̩͍̆͜ę̶̧̨̩̗̘͓͕̘̥͙̅́̈́̇͜͝ ̶̬̩͑͌̍̐̄͘̚͝l̷̳̗͇̊̃̒͒͑̚ḯ̵̱̖̩̈́̒̆̂͌̌̔͘͝͝͝b̶̢͚̘͚̟͖̣͆͑̇͗ŕ̷̨̧̛͕̱̯̙͎̙̪̦͓̲̓͊̽͒͠ą̷͔̠̑̈́̎͝r̶̛͉̰̝͍̖̔̅̋̔͆̽́̾͠y̴̨͚̘̪̖̙̘̙̜̘͚̾͋̋͑ͅ ̷̛̛̭̘̣͙͎̘̻̥̈́̀́̓̋̃͘͘͠ş̷̧̣͈̲͕̼͇́̏͌̐̉͌̔͊̂̀͘͠p̶̤͈̩̦̪̍͛͆̑̚ë̶̻̪̗̰́͐͜a̴͚̭̞̠̠̞̓k̴̦̻̜͈͉̖͇̠͓̓̆͂͌́̋̌̔̋͒͐͝s̷͓͚̙̟̫͇̳̫̜̭̓͋̀̽̋̿͐͋̀̋̚ ̸̨̧͚̣̘̔͝d̶͙̞̩̹̫̰̬͎̩͛ͅi̶̺̳̾̈́͗̋̕r̴͉͚̹̔̊̉̂̽̒̈́̈́͝͠ĕ̵̤̖̫̝̗̫͈̖̘͇̏̒̈́̋̔̀̉͘c̵̺̣̣̬̈́͋̈́͗̂̓̌͑̓̄̀t̸̪̬̋͂̽̓̈́̀̓̌͒͝͝l̴̳̯̲͔̯̦̥̙͙̺͐̉̐̊͛̽̀͛́͂͝ͅy̶̡̯͓̘͇͔̖̩̔̇̈́̇́͜͠ ̸̫̪͚̜̻̻̹͕̍͗̒̈̂̉̀̓͌t̴͖̥̭͖̬̭̲̯̜̖͊̀̈̃͑̋o̸̡̡͉͍̠̺͕̻͗̀̾̈͒̽͊ ̶̛̣̖̝̼̠̠̹̠̥͓̟̃̆͆̓̿̃̀͘ͅȳ̷̼͍̦̋̋o̸̻̟͗͋̐̌́͝ͅu̵̧̬͗͑̿̈́̆̀̍.̴̗̙͎͙͊͊̎\n\n\"̷̧̧̗̮͕̦̗̪͇͉͕̠̪̑̉͋̈́̇̔̌̈́͆͐̀́̇̆̈́̕̕ͅͅŴ̸̡̲̤͕̟̞̬͓͚̖͔̯̼͓͕͎̀̈́́̅h̵͙̱͛͛̎ͅë̷̢̨̠̫̩̣̖̯̭̣̳̫̠͕́̐̊̔͒̀̈͒̓̊̋͋̕̚͜͝͝n̷̛̞̤̥̮̗̹͂̓̽̓͋̍̉̽̆́̌̀̾͂̀͛̈́̊͒ ̸͈̣̠̯̤̹̭͈̳̠̮͋̂͋̄́͘ṯ̸̢͕̱̪̘̫̫̫̱̈̾̐̑̎̂̉̈́̾̌͂͌̚͜͜͠͝h̵̨̭͔͕̗̪̗̹͇̭̟̠̗̽̄̊̈́̿̾̾̅͛̿̐̽̀̄̀͊͋͋͝͝e̸͙͉̺̍̍͆̾͋̀͝ ̷̢͕͈̯̱͙̦̯̻͓͉͂̓͘w̸̡̛̉͐̈́̐͊͗̎͒͊̏̓̕͘͠͠ō̸͓̖̥͎̳̞r̷̡̢̛̙̣͙̯̮̦̘͉̹̬̠͚̣̤̟̞̫̰̋͌l̷̯̲̥̘̟̜̘͕̺̹̰̙̜̔̀̓̋͝d̴̯̬̦̰͈̥̟͈̜̳̣͉̹̓̅̇͋̈́̈́̔̈́̅̎̆͋͋̄̑͆͘͘͜͝ ̷̧̨̡̢̡͎̬̻͕̤̝͉͓̦̯̠̜͐̎̉̾̈́͐̊̔̚f̶̧̧͖̮̺̤̰̲̹̱̘͇̳̅͋ą̸̢̦̣͎̠̠̖̳̪͖̲̯̻̒̑̑̐̅̅̿͋͒̅̒̋̄͆̿̑̕̚͜ͅͅl̷̡̢̨̜̲̙͍͇̗͎͙̯͔̄̂͊̋̈͌͋̚͝͝͝ļ̶̧̛̛̥̳̤̲̱͎̞̠̣͋̀̎͆̈́̊̊̈́̍̌̊͑̚͘͜s̵̢̛̛̗̞͚̘̥̼̗̫̜̰͙̙̜̯̫͗͛̈̀̃̀̀̽͂͒̓̑͆̕̕͜͠ ̴̢̧̛̠̝̞̣̥̼͖̮̗̒͌̋͝͠ͅǫ̸̡̞̖̥͓̣̟̲̲͕̟͓̭̜̦͙͎̫̈́́̊̀ň̴̡̛̯̙͚̲͖̻͎̑̈́́̽̏̓́͑͘̕͝c̵̢̨̛͉̝͙̟͚̜͚̲̎̏ę̸̨̨̼̱̲̞̗͚̮̣̹̝̬̼͎͓͇̳͋͆͗̆̄͆͌̆̈́͌̏̿͘̕̕͝͠ ̵̳̬̖̗̠̻̰͍͕͎̭͇͙̜͖̜͕̘͚͍̐͛̌̾́̌̇m̶̧̨̧̧̧̧͔̭͙̼̻̟͖̝̞͋̀͋͋̑́̌͜o̶̡̩̭̻̍͗͗̌̃̂̔̕r̶̛͕͖̝̯̲̬͇̣̦͛̈́́̒͂͒̅̈̑̌͝͠ͅȩ̴̧̫̫͚͓̠͈̰͎̱̦͈͈͒̄̿̓̈́́̀̀̄̏͝ͅͅ,̷̢̼͖̝̮̤͈̀́͒̐̂͐͑̈̽ ̴̛̪͚̋̄͆̒͗̔̊̿̏͒́̚̕͝͝w̷͚̠͍͊͊é̷͇̘͓͕̟̩̯̳̭̼̞͔̱̔̇̒̂͊̈́̇̏͝͠ ̷̗̯̘͚͇̱̝̠̻̳̘̖̼̫̝̻̿͋̐̽͑͂̌̀̋̌̐͘̕̕̕͠w̷͍͇̞̬̻̯̬̣̭͙̜͋͛̔̋̋̅̄̃͌̇̒̿͝ĩ̵͍̘̣̲̦̍̕ļ̵̘̱͚̙̟͒̅̈́̎͆̒̏͆͂͆̕͘l̸̡̛̛̩̲͍̩̩̱̓̌̾̾̐͝͝ ̴̥̼̥̟͖̞̄̈̓̐͗̋̌͌͗r̵̢̺̯̤͇̩͚̟̲̖͍̠̝̂͌̓̀͑̅̊̕͠ͅĩ̵̧̳͈̤͙͉͇̦͇͍͉͇̑͆̔̋͌̔̈́̓̅̉͐͑̑͌͘͝ͅs̶̢̧̢͎͕͍̮̼̙͚̮̬͚̰̋̏̄̃̀͜͠ẻ̸̡̙̞͓̠͇͖̠̲͔̣̹̌͊̑̈́̃̋͗͗̓͘͠ ̶̡̡̻̼̤̻͓͋̒͘͠ư̵̡̠̦͍̱͍̱̳̹̩̲̳͈̻͍͎͗̅̂̏̎̈́͒̈́̈̄̕͠͝͠p̶̡̘̲̩̣͈͎̖͙̭͓̘͐̓͌̑̊͐͘̕ ̴̡̡̠̲̺͔̼̟̣̺̪̳̊̇̐͌͛͆͜͝ͅá̷̛̘̳̥̦̤̹̼̤̥̝̳̟̯͓͚̾͛̑̃̑͝͝ņ̶̨̱̼̳̠̠̬̻̞̮̙̖̻̫̤̰̻͇͛̈́̋̐ͅḑ̸͎͖̰͓̝͈̟̠̺͍̘̺̞̣̖̏͘ͅ ̸̛̲̟̟̣͇̟̗͚̲̐̈́̀̔̕̚ͅt̵͙̥̹̭͚̝̞̯̰̱̫͎̹̓́̔͊̀͗̃̾̔̀͠á̵̢̢̼̮͍͇̯̘̝̹̟̗̫̟͍̙̙̗͖̗̘̽̐̾̈́̀͠k̶̹̱̄͋́͒̄̽̏̒͆̐̔̂̀͛͘͘̕͝͝ẽ̴̞̮̝͒̃̅́̋̿̏̈̈́̋̕̕͠͝͠͠ ̷͇̹͇͇̠̙̠͂͑̑̍̓ͅb̵̛̟̦͍͍̣̮̞̖̫̻̫͕͕̺̌͘͜ą̸̨̧̛͉͕͍̖̥̯̲̮̬̈̿͊̌̊̂̑̀́̌̽͛̍̓̈́̕͠͠c̷̫̭͌̆̚k̴̨̧̛͎̺̐͌̒̌͐͛͂͂̿̈́͐͆̚̚͝ͅ ̵͈̼͂̏̈̓ţ̸̡̧̢̹̤̘͖͕͇͍̜͇̖̜̾͂ͅḩ̷͖̣͍̬͈͚͈̤͛͊͗͌̅̓͠͝ę̶̫̣̠͙̬̣̤́̀̐̓ ̴̢̠̦̯̗̳̯̙̥̭̐̈́̃̑̀̃͊͑̇͑͒̍̌̾̌̇̕͝ç̵͓̞͚̟̯̹̝̮̘͚̖̜͇̂̌̽̈͐̿̓̀͑̕͠͝r̷̛͙̐̿̈́̈̃͆̐̈̉̊́̉̔͊́̄̑͐ö̴̢̧̧̺̬̪̹̰̗͇͚̪̰͔̼̠̰̦̫̞̮́͆̅͛̋̀͒̆͝w̶̧͎͉̱̙̑́͋̈̌̇̍̉̏̏͛̈̾͊͘͘̕͘͝͝n̵̡͙͚̮̱̮̫̺̻̤̫̟͉͉̗̘̭͓̗͋͜.̶̨̬̲̙̤̻͖̟̗̞̲͚͚̥͔̗̙̮͌̀̽̿̍͜͜ͅ ̸̡̧̛̻̠̼̜͚̪͕̜͍̤̠͋̊̃̌̿͂̉̚͠͝K̶̢̧̧̡͚̹̖̜̰̤͎̜̲̣̓̊͌͌̅̽̈́͂n̷̠̘̙̲̫̯̬̿̽̔͂̒̓̏͛̄̾͛̓̓͠ͅỏ̵̢̩̰̦͍̰̜̝̰̰̤̞͉̜̞̙̤͖͂̌̈̊͂͑̉̀̇̀̋͐̊͛͋͘͘̚͝ẘ̸̥͚̰̙͍̻͖̭̠͖̿̂̽̀ļ̷̛̘̝͇͈͛̌̃̊́̽̽͐͌̏́͛̌̆̊̉͘̕͝͝e̶̢̨̫̥͕͍̠̗͕̥̬͇̒̔̐̒͂́̆͌̆̀̀͂̀͗͊͋͗͘͠d̷̹̣͙̗̙̮͈̝͙̟͍̥̩̮̤̻̮̳͍̭̓̃̊̓͗̇̽̑̐͑́͠g̸̬̺̰̺̫͕͎̥̯̪̩̦̖̳̮̣̼̟͛̓ͅé̷̡̨͓̯͓͚͕͖̹̠̼͉̄ ̶̧̢̙̗̪̙͍̣̘̞͈̫͎̼̘̣̱̣͉͊̀̊́̍̈̎͒̓̆͋̍͂̃̑̽̕͠͠ì̶͕̱̜̮͙̰͔̞̝͕͈̖͔̰̥̦̼̬̂̽́̏̆̑̔͐̚̚̚͝͝͝͝ͅs̷̻̜̰̖͇̹̪̣̪͈̙̺̼̟̦̜̔̈̌̑̓͘͘͜͜͝ ̸͕̤̖̗̟̙̗̦̖̞̞̭̺̮̃̒͘͘ͅt̴̢̬̪̠̀̽̈̎̾̈́̏̄̋ḩ̷̙̟̺̦̥̲̈́̊̈́̊͂̒̆͋ͅe̵̺̫͉̲̣̹̎̇͊̓͋́̈́͑͗̓̄́̅̀̚̕͘̕͠͠ ̵̢͕̩̹̬̭̘̻̥͔̱͍̇̒̅͗͊̂̈́̈́̌̾̈́̂͋́͜͝͝ͅe̶̢͖͚̦̻̹̹̼̗̗̻̦̋̊͂̆̿͂̈́̇͘ͅn̷̢̳̺̙̩͌͑͆͋̅̾ę̶̡̙̯̳̘̙̞͎̯̠̲̦͙̄́̌̑͂̈́̊͋̾͋̿́͐͛͛̿̈́̈́͠͝͝m̸̛̭̮̥̝͕̰̤͚̯̅̾̋͌̅̋͒͐͊̀̋̓͌̑̀̚͝y̶̧̥͉͎̘̟̟̳͔̬̳͈̣̲̼͐̈͌̈̍͗͐̾̋͌͑͑̚ ̸̨̨̧̨̡̧̨͙̞̫̮͖̼͇̘͖͔̘͙̲͌̋̈́̀͜o̶̰̘͙̼̰̙̗̬̙͔̭̲̰͓̩̩̊̄̀̄̎̑͒́̔̃̀̐͋̈́̉͘͜f̸̛̛͎̱̞̣̖̼̺̟͓͖̱̭̖͔̭̙̩̲̾̇̍̒̔̐̅͜ͅ ̶̡̢̲̠̩̠̯̭̭̬̦̩̥̦̯̰̦̃̀͋͆̎͊̽̊͊̅̏̔̅̀̂͆̕͝͠͝ͅd̵͇̩̞̥̹̀̓͂͌̽̏͜ė̶͉̩̪̜͔̝̟̪̻̼̟̌̈͜͠ͅͅa̸̛̺̲̻̭̭͔̾̓͗̾͒̀̐͋ͅţ̴̛̝̰̔̎̋̊͊̅̑̌̑̿͛͂̚͘͝͝͝͝͝ḣ̵̡̡̧̺͙̮͇̟̳̼͕̝̰̖̜͎̫̣̭͎̈́̕͝.̸̨͈̿͛͂̽͋͜ͅ ̸̢̞̤̖̦͎͙͚̊̀̿͑̀̆̎̉͘͝ͅṠ̸̰̥̱̤̤̣͉̱͋̂ȯ̶̡̧̨͎̳̣̼͚̲̙̮̹̯̬̳̰͉̹͔̖̅̀̍̓̏̒͘ ̷̢̠̩̰̥̙͙̠̰̘͎͓̐̒ͅw̵̢̨̞̞͕͔̯̞̠̺̦̜͈̫̣̹̼̝̗͂̈́́̈́̌͗̂̉̈́̐̄̑̐̿͘͠è̵̬͙̖͍̲͕́͘͜ ̸̨̣͉͎̙̗͙̯̗͖̮̮̼͕͈̍́̂̐̓̀̓̋̂͜w̶̧̧̺͖̰̮̹͓̲͔̥̟̼͗́̈͊̀̈̽̿͒̕̕͠ͅi̵̛̞͂̎͆̐̈́̇̓̍͒̀̏́͆̌͌͘͜͝͝͝l̷̨̢̡̨̡̗̖̞̮̹͖͇͚̯̲̉͒̒̚͜ͅͅl̴̙̩̇͛͌̃̆̅͗͋́̈́̏͂͋̅̎͂̆͝͠͝ͅ ̶̢̢̣͔̟͚͓̖͙̱̪̘̫͇̪̙̱̦̰̻͒͋̀̔͊̌͝͠͝͝l̷̢̥͕̻̹̯̝̙̘̥͙̺̟͈̻͌͆̔͛̉̓̀̚͘ĩ̴̦̩̪̜͙̟͙̮̍͌́͆̀̆̕v̶̧̺̟͕̆̃ȩ̸̛̛̅͊͆̽͂̓̐̆͝ ̸̢̝̪̪̥̼̺̦̯̖̫͉̮͔̰͍͚͎͔̳͗͒f̶̡͛̚ơ̵̗̱̳̖͖̎̂̅͌̍̕r̵̝͚͓̹̦͐͋͛̀͒̄̋̑͗͒́̔̐̒̋͘ȩ̶̧̢̳̫̹͕̭͍̖̗̳̼̜̙̞͈̀̅͊͝͝ͅv̵̨͇͙̩̖͉͚͈̈̐̃ȩ̵̪͉͍̯̳̤̯͔͕͇̖̖͆̔͛́̂̎̾̓̂̅̎͆̑̚͘͘͜r̵̫̝͇̻̘̯̘̞̻̮̦̪̣̹̠̝̤͈̖̳̾.̸̢̡̖̟̬̱̼̹̬͈̗̠̙̉͗̅͆̔̅̈́\"̵̢̨͚̱͉̦͖͈̯̗͔͇̲̣̈̂̔͗̊̐͝\n\n\n\n[[CONTINUE|A goal reached]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "A goal reached",
          "original": "[[CONTINUE|A goal reached]]"
        }
      ],
      "hooks": [],
      "cleanText": "A̴s̷ ̴y̶o̴u̶ ̷e̴n̵t̷e̵r̷ ̸i̸n̷t̵o̵ ̶t̶h̶e̵ ̶r̶e̷s̸t̴r̵i̷c̵t̷e̷d̸ ̸s̴e̸c̴t̷i̶o̶n̶ ̸o̴f̴ ̶t̴h̷e̵ ̵l̷i̴b̶r̶a̶r̶y̸ ̴y̴o̴u̵ ̷c̸a̸n̷'̴t̷ ̴h̴e̷l̷p̶ ̴b̷u̷t̷ ̶s̸m̸i̶l̷e̵ ̶a̶s̸ ̸y̷o̶u̴ ̸h̶e̸a̶r̴ ̷t̶h̵e̶ ̸d̵a̵r̷k̵ ̵w̴h̵i̶s̴p̶e̷r̸s̶ ̷f̵r̷o̶m̴ ̶a̷l̴l̶ ̴t̶h̶e̴ ̶f̵o̵r̵b̷i̵d̷d̷e̴n̶ ̸t̴o̷m̸e̵s̴.̷ ̶T̴h̴e̵y̷ ̵b̵e̷c̷k̵o̴n̷ ̴t̷o̴ ̵y̶o̷u̶,̷ ̵b̸r̴i̸n̸g̸i̷n̸g̴ ̷y̵o̴u̷ ̵d̵e̴e̴p̵e̴r̸ ̵i̴n̶t̶o̶ ̵t̵h̶e̶ ̸f̴o̶l̸d̷s̴ ̸o̷f̶ ̶k̸n̴o̷w̷l̴e̶d̷g̷e̶.̴\n\nY̶̞͔̗̟͝o̸̲̬̹͘ṳ̸̹̳̱͘ ̴͓͎̹̝̙̆̏͘ͅa̷̗͌̐̈́̍͝r̴̙̣̊͆͂͋͠͝e̴̢̮̮͇͖͑͂̒͠ ̵̞̓̋̓͂͘͝t̵̨̯̿̃̓á̷̛̙̫͕͔͓͌͜k̴̮̪̪̙̽̾̽͝e̴̞͈̞̖͗͑n̶̻͛̈́ ̸̘̠̅̈́ì̴͇̹͍̗̮̾̎n̶͍̿͋̈̉̚͠t̵̟̞͑͘͘ò̵̡͚͓͙ ̴͙͉͖͇̳͍́̐͝͠t̶̲͐h̶̝̘̠̃ĕ̸̡͚̳̯̻̈́̎͜ ̷̢̍f̵̖̞̯̿̽̽͒̒̕ó̵̮̪̬̯̝́̀̅̃l̷͔̈̆d̷̫͈́͂s̴̛͚̦̝̜͉̈́͂͂̿͝ ̷̢̝̹͉͉̪̽̈͘͝ȏ̴̦̝̖̔̆͑f̸̢͎̮͇̜̆̏̓̂͠͝ ̵̪̱͖̀͆͆̚ṭ̸̉͂͐̽͜h̴͍̱̤̮̝͆̂̒͒e̷̼͈͕̥̗̻͊̈́ ̵͚̀l̶̪̮͚͚͉͍̔̌i̵̡͔̟͓̪͊ͅb̵̫̰̙̤̭͈̏͒͐͌r̴̤̠̤͚͉̂̐͘ȧ̷̛͙̪̮͎̽̚͝ŕ̸̮̇͂y̶̰̞̮͗̅.̸̨͇͍̥̕ ̸̫̼̘̠͇͍͂̎͗̈́̉I̶͍͉̩̭͚͎̽͊̽̋ț̷̭͆͊̑ ̴̥̫̭̪̲̎́̌́̕ẅ̴͎̥̗̭̺́͌̚̚ḩ̸̥̻͙͉̺͌͒͂̓͘ḯ̷̟̭̪̙̅s̷͈͙̟̒p̸̗̎͊e̷̢͂̉͛ŗ̵̧̠̙́̏̍͘ͅs̶̤͚̤̓̈́͘̕͜͠ ̷͚͙̻̋͆e̶̡͔̤̦̝̒̆̀͒̔ṉ̵̖̣͔̣̂d̴͚̪̠̆́͂l̶̫̠̠̜͕̪̽̓͒ë̸̛̹́̓̽̇̚s̶̛̥͖̱͆̐̕̕͝ͅş̸̯̘̰̼͖͒l̷͓͉̱̙̓̍͌̈́̐̾ỹ̴̌̒͊̈́͠ͅ ̴̢͍̘̯̲̓̔͠i̴̻̰͠n̶͔̺̻̦̑t̵̻̘̅͐̋̿ō̸̹͓͂̀̄̌ ̸̮̖͑̑̈́͗͝y̶̧̛͚͉̤̿́o̷̩̾̑̕͝ụ̸͍͚͖͕̅̿͐̽r̶̢̯͊̓̊͌̄͐ ̶̲̥̦̔͊̓̂ě̷̛̹͛̀̈́a̵̱͑͜r̷͖̭̱̱͉̀̌̍͑̚̚ͅs̷̙͕̏,̸̰͇̥̦̺̯̏̄̈́ ̶̛̼̯͎͕̲͗͗̐͘̕t̴̺͇̥̘̗͍̍̿̋̇̃̒ę̸̨̩͚̟͂̔̒͑͂̒l̸̜͆̃̑l̶̢̻̳͓̳̈́̃̑͜ḯ̸͎̫̲͘ņ̸̝̐̍̕͘g̴͎̏̏̀̒͛̈́ ̸̛͈̭͚̈̀y̶͔͙͒͊̋o̷̼̗͕̼̿͋͋͑̐͜͝ṷ̵̳̗͐̈̔̎̏ ̴̧͈̟̈́̓͊̎a̶̝̺̲̫̫̍͛n̵͙̘̕c̶̤̈ȋ̴͓̪̅͌̕e̸̢͓͔̙͍͛͝ņ̷̗̖̭̣̟̀̽͊̓̓̂ẗ̸̖̻͗̃̔̆̽ ̸͖̞̃a̴͎̐̅̚n̷̰̹̜̜̱͊d̷͙̱̹̆͝ ̵͓͂̎̈́f̷̡͍͓̆ò̷̢̘͕̄͠͠ͅr̵̮̙̉͐͂b̵̺̮͉̕̕ḭ̷̓d̷̖̼̠͉̜̖͗d̴̨̮̣͔̜͂͛͊͂͒ȩ̵̞̄n̸̬̥̿ ̵̨̜͇͙̍̊̄̀t̴̨͙͔́̆̓̏h̸̢̳̙̙̆̆͌͋̈́͝ǐ̶͙̭͉̊̚ṉ̷̺̪͈̂̒̍ĝ̶̮̫́̅ş̷̠̌̈́͋͝.̵̞̌̍̀ ̶̖͓͈̔Y̴̻͕̺̟͊͐͊͝ọ̸͚̗̋̾͛̔ů̷̟̆͐r̸͖͘ ̸̡̎͆͆̆́̓m̸̤̎̚͜͝ỉ̶͍́́̉͘n̷̡̢̳̬̍̃d̵̬̿ ̸̬͊̀̔̅͒̐c̶̡͓̪͓̦͛̈͂͌̿å̴̠̞̉͐̈́͌̽n̸̤̞̯̪̼̿̾̕͜ ̵̛̱̞̜̾̐̚b̵̖̥̬̘̘͍̿͝a̶̙͋̅͌̏͌r̴̩̯̆e̵̯̯̺̙̖̔̐͛l̷͍̻̦̖͎̂̓̓̄͑͘y̵̖̰̋̾̍̿̚ ̷̗͇͇́͂̈́h̵̺̓́́ä̸̝́ń̵̙̳̜d̴̢̼̂l̸̜̠̫̻͙̓͐e̴̛͖͛̾ ̴̢͈̠̭̇̎̂̊͛͂i̴̤͈̜̮̇ț̷͇͙̥̬̤́̋.̷̢̝̭͙̮̓̆̈́ͅ ̴̠͚̪͐̽̂\n\nD̶̯͍̝̤̥̦͈̞͍̙̥̈̇̈͜ë̸̡̳̟̺̮̦̣̞̘̟́̽̈́͆̏̈͐̊̀͊̕͜ḛ̶̝͍́͗̀̄̑p̷̢̖̻̼̟̹̿̽̄͑ȩ̶̫̭͕̎̽͋͗̏͐̊͘͝͝r̴̡̤̭͎̮̓̀̔ ̶̲̇̂̔͂̿ă̴̲̪̯͓̰͖̣͇̿̽͂̓͑̂̔̒͛͐͜͠ǹ̴͙̦̳ͅͅd̶̜̲̥̊ ̵̤͚̳͕̺̪͇̰̟̂̅͒͊̕̕̕ͅḋ̸̡̡̹̜̳̫̪̮̩̣͊̈̂̃̿͂͠ẹ̷̩̯̤͊͛́͐ė̴̤̞̬̙͙̻̱̤͔͊͛ṕ̸͚̼̍̇̈́̇̈́̒̌́̇ḙ̷̏̂́̃́͑r̵̛̰̰̱̤̭̘͚̥̯͊͊̏͒̽͛͂̕͝͠,̴̢͔̥̘̝̏͑̅̊̊͘ ̵̡̙̬̤͍̈́͆̽́̈̃̿̊̎͌y̸̨̛͔̯̭̦̌̉̔̒̄̋̋̿̐̂̕ͅo̸͍̗̣̜̙͓̼̻̤̅͊ǘ̵͚̯̖̙̾̋̀ ̴̨̢͎̫̜͙̯̬͇̎̆̈̏̎̈̕̚͜ḑ̶̧͙̬̜̯͚̰͆͒͒̔͗̈͋̅̏́e̸̡̼̫̯͕͈̥̟̯̼̿͐̔̐̊̊s̷͇̜̈́ç̸͎̗̦͕̪̳̫̔̊͑͘é̶̗͚̞̪̺͜n̶̳̹̝̲̊̍͠͝ͅd̸̯̥̲̗̹̲͚̘͋̒͑̕̚.̷̟̜̦̙͚̮̜̗̽͑̈́͒̐͛̋ ̷̛͇̳̥̫̻̟̥͚͈̈́́̎̌̏̔̑̊̽͝͝ͅͅÁ̷̰̣̠̤̺͎͕̩̣͓͓̆̊̇ͅļ̷̛̩̣̯̊͌̿̃́͘ľ̸̩̩̜͓̯̱͕̗͙̼̤͖̀̄̍͒͛̇͊̎ ̸̢͙̞͖͕̃̏̆͐̓̐̽̓͑͘͝ţ̴̧̩̣̞͖̠͔̟͉̫͙͝ḧ̶̡̭͚̖̣͎̰͓̲͉̹́ę̶̧̜̲͕̺̎́͛͜ ̵̫͇͙̲̫̺̠̘̓͐̊͜͝w̷̟̪͂̑͑̃̎̓͘͘a̵̧̡̢͝ÿ̵̼̹͌̔̂̿̌͌͠ ̴̛͈̼͕̼̥͒̋̈́̂͛̈́͛̀͘̚͜i̸̖̯͚̒̈̏̉̆͑͐͊́̚ņ̴͕̳͔̼̫͙̠͕̀͐͆̈͌́̓͛͜͠͝ͅt̸̛̙͖͚̲̍͋͐̂͒́͗̈́̈͋̕ͅo̸̻̙̎̆̋͑̑̾̉̿͘̚͘ ̸̤̥͇̘͌͌͜t̴̥̳̥̱̦̻̭͍̦̝̤̿̈́̑̀̑͠h̷͇͕̻̤̣̘̥͓̺̝̲̤̐̄̑̓̓̓͋̈e̵͈̮̘̹̭̻͌̉ ̷̙̻̘̤̹̝͛̆̈́̿̈́͑͛̈́̊͛͝͝ḩ̷̡̡̰̹͓̘͓̩̳̭͉̀̓è̵͚̭̜̙̃͋̾͆̒͘͘͘̕͜͝ã̷͓̱̲͎̲͈̜̮̐̕r̷̬̻̰͆̀͠ṱ̷̨͙̹̘̩̺̜͋͛́͊ ̶̰̘͋͋̂̾ǫ̷̨̯͈̫̪̘̰̗̙̦͂̀̽̆̒̊̂f̸̧̡̖͙̘̲͍̭͕̦̬̪͒́ ̷͚̰̠͔̟̫̖̌̄͐ţ̶̨̠̤͓̮͙̬͈͆̍̏͐̄̐́͋͂h̵̰̹̹̱̩̮̠̟̦̆̓͑̈́̊͠ḝ̶̧͔̟͚͍̱͙̫̙́́ ̶̡̛̰͎̀̈́̉͒̍̏̏̋̐́̕l̵̥̭̼̩͍̗̎̃̍͊̔̈̿̎͝͝ị̸̲͙͛͂̿́̽̓͒͒̇̾͘͜b̷̜̞͉͇̩̫͎͖̦͙͂̈́͛̕͜ŗ̸̹̬͎̲͗̍̀͒̓̌̈̄́̚͠ͅạ̷̡̗͚̬̰̍r̶̩̙͈͐́ÿ̴̛̛̘̥̖́́̂̈́̔̊̋͊̐̋.̵̘̙̦͓͔̜͙̐̈́̈́͆ ̸̡̡̫͈͓̳̲͖͕̫̊̀̉́̈́̆̃͋̇͛͠ͅṪ̴̢̲̦̯̗̃̇̂͂̿̄͆̎͘͘ͅĥ̸̨͙̲̼̇̍̓͂̓̉̈́̂̄̇̀e̵̳̬̪̗̯͇̯͕̍̃̑̒̍̍̈͌͒̃ ̸̝̲͎̟̀ͅd̴̢̞̤̦͍̽̀̀̏̄͑͐͘a̵̮̣͚͓̎͒̂̍̒͜r̵̨̢͎̭͎̺̙͆ͅḱ̵̤͙̠̮͊͆̔ͅ ̶̛̳͕̬̙͚̣̎́̋̌͋̀̒̇͛m̷̫̀̋̊͂i̸̙̭̱͇͚͍̲͆͐̌̃́͋͝͝n̵̡̡̢̧̤̜̼̺̲̜̣̏̅́̈̈́̋̍͜͠͝d̶͇͎̺̺̰̂̑̂́̃̀̓͒̊͌̓̎ ̵̖̗̝̖̈́̂̌͠ọ̶͓͉̻̰͉̣̞͍̳̭̑́͑̒͜͝f̵̨̣͓̘͈̼̟̲̫̜̍̎̃͂̎̉̇̚ ̷̬̈̽̾̐̽̊͠t̷̢͓̼̹͎̖̥̘̺̝̟̘̅͂͆́͊̏͆̔̈́͘h̷̡̨̫͚̰̤̰͔̩͍̆͜ę̶̧̨̩̗̘͓͕̘̥͙̅́̈́̇͜͝ ̶̬̩͑͌̍̐̄͘̚͝l̷̳̗͇̊̃̒͒͑̚ḯ̵̱̖̩̈́̒̆̂͌̌̔͘͝͝͝b̶̢͚̘͚̟͖̣͆͑̇͗ŕ̷̨̧̛͕̱̯̙͎̙̪̦͓̲̓͊̽͒͠ą̷͔̠̑̈́̎͝r̶̛͉̰̝͍̖̔̅̋̔͆̽́̾͠y̴̨͚̘̪̖̙̘̙̜̘͚̾͋̋͑ͅ ̷̛̛̭̘̣͙͎̘̻̥̈́̀́̓̋̃͘͘͠ş̷̧̣͈̲͕̼͇́̏͌̐̉͌̔͊̂̀͘͠p̶̤͈̩̦̪̍͛͆̑̚ë̶̻̪̗̰́͐͜a̴͚̭̞̠̠̞̓k̴̦̻̜͈͉̖͇̠͓̓̆͂͌́̋̌̔̋͒͐͝s̷͓͚̙̟̫͇̳̫̜̭̓͋̀̽̋̿͐͋̀̋̚ ̸̨̧͚̣̘̔͝d̶͙̞̩̹̫̰̬͎̩͛ͅi̶̺̳̾̈́͗̋̕r̴͉͚̹̔̊̉̂̽̒̈́̈́͝͠ĕ̵̤̖̫̝̗̫͈̖̘͇̏̒̈́̋̔̀̉͘c̵̺̣̣̬̈́͋̈́͗̂̓̌͑̓̄̀t̸̪̬̋͂̽̓̈́̀̓̌͒͝͝l̴̳̯̲͔̯̦̥̙͙̺͐̉̐̊͛̽̀͛́͂͝ͅy̶̡̯͓̘͇͔̖̩̔̇̈́̇́͜͠ ̸̫̪͚̜̻̻̹͕̍͗̒̈̂̉̀̓͌t̴͖̥̭͖̬̭̲̯̜̖͊̀̈̃͑̋o̸̡̡͉͍̠̺͕̻͗̀̾̈͒̽͊ ̶̛̣̖̝̼̠̠̹̠̥͓̟̃̆͆̓̿̃̀͘ͅȳ̷̼͍̦̋̋o̸̻̟͗͋̐̌́͝ͅu̵̧̬͗͑̿̈́̆̀̍.̴̗̙͎͙͊͊̎\n\n\"̷̧̧̗̮͕̦̗̪͇͉͕̠̪̑̉͋̈́̇̔̌̈́͆͐̀́̇̆̈́̕̕ͅͅŴ̸̡̲̤͕̟̞̬͓͚̖͔̯̼͓͕͎̀̈́́̅h̵͙̱͛͛̎ͅë̷̢̨̠̫̩̣̖̯̭̣̳̫̠͕́̐̊̔͒̀̈͒̓̊̋͋̕̚͜͝͝n̷̛̞̤̥̮̗̹͂̓̽̓͋̍̉̽̆́̌̀̾͂̀͛̈́̊͒ ̸͈̣̠̯̤̹̭͈̳̠̮͋̂͋̄́͘ṯ̸̢͕̱̪̘̫̫̫̱̈̾̐̑̎̂̉̈́̾̌͂͌̚͜͜͠͝h̵̨̭͔͕̗̪̗̹͇̭̟̠̗̽̄̊̈́̿̾̾̅͛̿̐̽̀̄̀͊͋͋͝͝e̸͙͉̺̍̍͆̾͋̀͝ ̷̢͕͈̯̱͙̦̯̻͓͉͂̓͘w̸̡̛̉͐̈́̐͊͗̎͒͊̏̓̕͘͠͠ō̸͓̖̥͎̳̞r̷̡̢̛̙̣͙̯̮̦̘͉̹̬̠͚̣̤̟̞̫̰̋͌l̷̯̲̥̘̟̜̘͕̺̹̰̙̜̔̀̓̋͝d̴̯̬̦̰͈̥̟͈̜̳̣͉̹̓̅̇͋̈́̈́̔̈́̅̎̆͋͋̄̑͆͘͘͜͝ ̷̧̨̡̢̡͎̬̻͕̤̝͉͓̦̯̠̜͐̎̉̾̈́͐̊̔̚f̶̧̧͖̮̺̤̰̲̹̱̘͇̳̅͋ą̸̢̦̣͎̠̠̖̳̪͖̲̯̻̒̑̑̐̅̅̿͋͒̅̒̋̄͆̿̑̕̚͜ͅͅl̷̡̢̨̜̲̙͍͇̗͎͙̯͔̄̂͊̋̈͌͋̚͝͝͝ļ̶̧̛̛̥̳̤̲̱͎̞̠̣͋̀̎͆̈́̊̊̈́̍̌̊͑̚͘͜s̵̢̛̛̗̞͚̘̥̼̗̫̜̰͙̙̜̯̫͗͛̈̀̃̀̀̽͂͒̓̑͆̕̕͜͠ ̴̢̧̛̠̝̞̣̥̼͖̮̗̒͌̋͝͠ͅǫ̸̡̞̖̥͓̣̟̲̲͕̟͓̭̜̦͙͎̫̈́́̊̀ň̴̡̛̯̙͚̲͖̻͎̑̈́́̽̏̓́͑͘̕͝c̵̢̨̛͉̝͙̟͚̜͚̲̎̏ę̸̨̨̼̱̲̞̗͚̮̣̹̝̬̼͎͓͇̳͋͆͗̆̄͆͌̆̈́͌̏̿͘̕̕͝͠ ̵̳̬̖̗̠̻̰͍͕͎̭͇͙̜͖̜͕̘͚͍̐͛̌̾́̌̇m̶̧̨̧̧̧̧͔̭͙̼̻̟͖̝̞͋̀͋͋̑́̌͜o̶̡̩̭̻̍͗͗̌̃̂̔̕r̶̛͕͖̝̯̲̬͇̣̦͛̈́́̒͂͒̅̈̑̌͝͠ͅȩ̴̧̫̫͚͓̠͈̰͎̱̦͈͈͒̄̿̓̈́́̀̀̄̏͝ͅͅ,̷̢̼͖̝̮̤͈̀́͒̐̂͐͑̈̽ ̴̛̪͚̋̄͆̒͗̔̊̿̏͒́̚̕͝͝w̷͚̠͍͊͊é̷͇̘͓͕̟̩̯̳̭̼̞͔̱̔̇̒̂͊̈́̇̏͝͠ ̷̗̯̘͚͇̱̝̠̻̳̘̖̼̫̝̻̿͋̐̽͑͂̌̀̋̌̐͘̕̕̕͠w̷͍͇̞̬̻̯̬̣̭͙̜͋͛̔̋̋̅̄̃͌̇̒̿͝ĩ̵͍̘̣̲̦̍̕ļ̵̘̱͚̙̟͒̅̈́̎͆̒̏͆͂͆̕͘l̸̡̛̛̩̲͍̩̩̱̓̌̾̾̐͝͝ ̴̥̼̥̟͖̞̄̈̓̐͗̋̌͌͗r̵̢̺̯̤͇̩͚̟̲̖͍̠̝̂͌̓̀͑̅̊̕͠ͅĩ̵̧̳͈̤͙͉͇̦͇͍͉͇̑͆̔̋͌̔̈́̓̅̉͐͑̑͌͘͝ͅs̶̢̧̢͎͕͍̮̼̙͚̮̬͚̰̋̏̄̃̀͜͠ẻ̸̡̙̞͓̠͇͖̠̲͔̣̹̌͊̑̈́̃̋͗͗̓͘͠ ̶̡̡̻̼̤̻͓͋̒͘͠ư̵̡̠̦͍̱͍̱̳̹̩̲̳͈̻͍͎͗̅̂̏̎̈́͒̈́̈̄̕͠͝͠p̶̡̘̲̩̣͈͎̖͙̭͓̘͐̓͌̑̊͐͘̕ ̴̡̡̠̲̺͔̼̟̣̺̪̳̊̇̐͌͛͆͜͝ͅá̷̛̘̳̥̦̤̹̼̤̥̝̳̟̯͓͚̾͛̑̃̑͝͝ņ̶̨̱̼̳̠̠̬̻̞̮̙̖̻̫̤̰̻͇͛̈́̋̐ͅḑ̸͎͖̰͓̝͈̟̠̺͍̘̺̞̣̖̏͘ͅ ̸̛̲̟̟̣͇̟̗͚̲̐̈́̀̔̕̚ͅt̵͙̥̹̭͚̝̞̯̰̱̫͎̹̓́̔͊̀͗̃̾̔̀͠á̵̢̢̼̮͍͇̯̘̝̹̟̗̫̟͍̙̙̗͖̗̘̽̐̾̈́̀͠k̶̹̱̄͋́͒̄̽̏̒͆̐̔̂̀͛͘͘̕͝͝ẽ̴̞̮̝͒̃̅́̋̿̏̈̈́̋̕̕͠͝͠͠ ̷͇̹͇͇̠̙̠͂͑̑̍̓ͅb̵̛̟̦͍͍̣̮̞̖̫̻̫͕͕̺̌͘͜ą̸̨̧̛͉͕͍̖̥̯̲̮̬̈̿͊̌̊̂̑̀́̌̽͛̍̓̈́̕͠͠c̷̫̭͌̆̚k̴̨̧̛͎̺̐͌̒̌͐͛͂͂̿̈́͐͆̚̚͝ͅ ̵͈̼͂̏̈̓ţ̸̡̧̢̹̤̘͖͕͇͍̜͇̖̜̾͂ͅḩ̷͖̣͍̬͈͚͈̤͛͊͗͌̅̓͠͝ę̶̫̣̠͙̬̣̤́̀̐̓ ̴̢̠̦̯̗̳̯̙̥̭̐̈́̃̑̀̃͊͑̇͑͒̍̌̾̌̇̕͝ç̵͓̞͚̟̯̹̝̮̘͚̖̜͇̂̌̽̈͐̿̓̀͑̕͠͝r̷̛͙̐̿̈́̈̃͆̐̈̉̊́̉̔͊́̄̑͐ö̴̢̧̧̺̬̪̹̰̗͇͚̪̰͔̼̠̰̦̫̞̮́͆̅͛̋̀͒̆͝w̶̧͎͉̱̙̑́͋̈̌̇̍̉̏̏͛̈̾͊͘͘̕͘͝͝n̵̡͙͚̮̱̮̫̺̻̤̫̟͉͉̗̘̭͓̗͋͜.̶̨̬̲̙̤̻͖̟̗̞̲͚͚̥͔̗̙̮͌̀̽̿̍͜͜ͅ ̸̡̧̛̻̠̼̜͚̪͕̜͍̤̠͋̊̃̌̿͂̉̚͠͝K̶̢̧̧̡͚̹̖̜̰̤͎̜̲̣̓̊͌͌̅̽̈́͂n̷̠̘̙̲̫̯̬̿̽̔͂̒̓̏͛̄̾͛̓̓͠ͅỏ̵̢̩̰̦͍̰̜̝̰̰̤̞͉̜̞̙̤͖͂̌̈̊͂͑̉̀̇̀̋͐̊͛͋͘͘̚͝ẘ̸̥͚̰̙͍̻͖̭̠͖̿̂̽̀ļ̷̛̘̝͇͈͛̌̃̊́̽̽͐͌̏́͛̌̆̊̉͘̕͝͝e̶̢̨̫̥͕͍̠̗͕̥̬͇̒̔̐̒͂́̆͌̆̀̀͂̀͗͊͋͗͘͠d̷̹̣͙̗̙̮͈̝͙̟͍̥̩̮̤̻̮̳͍̭̓̃̊̓͗̇̽̑̐͑́͠g̸̬̺̰̺̫͕͎̥̯̪̩̦̖̳̮̣̼̟͛̓ͅé̷̡̨͓̯͓͚͕͖̹̠̼͉̄ ̶̧̢̙̗̪̙͍̣̘̞͈̫͎̼̘̣̱̣͉͊̀̊́̍̈̎͒̓̆͋̍͂̃̑̽̕͠͠ì̶͕̱̜̮͙̰͔̞̝͕͈̖͔̰̥̦̼̬̂̽́̏̆̑̔͐̚̚̚͝͝͝͝ͅs̷̻̜̰̖͇̹̪̣̪͈̙̺̼̟̦̜̔̈̌̑̓͘͘͜͜͝ ̸͕̤̖̗̟̙̗̦̖̞̞̭̺̮̃̒͘͘ͅt̴̢̬̪̠̀̽̈̎̾̈́̏̄̋ḩ̷̙̟̺̦̥̲̈́̊̈́̊͂̒̆͋ͅe̵̺̫͉̲̣̹̎̇͊̓͋́̈́͑͗̓̄́̅̀̚̕͘̕͠͠ ̵̢͕̩̹̬̭̘̻̥͔̱͍̇̒̅͗͊̂̈́̈́̌̾̈́̂͋́͜͝͝ͅe̶̢͖͚̦̻̹̹̼̗̗̻̦̋̊͂̆̿͂̈́̇͘ͅn̷̢̳̺̙̩͌͑͆͋̅̾ę̶̡̙̯̳̘̙̞͎̯̠̲̦͙̄́̌̑͂̈́̊͋̾͋̿́͐͛͛̿̈́̈́͠͝͝m̸̛̭̮̥̝͕̰̤͚̯̅̾̋͌̅̋͒͐͊̀̋̓͌̑̀̚͝y̶̧̥͉͎̘̟̟̳͔̬̳͈̣̲̼͐̈͌̈̍͗͐̾̋͌͑͑̚ ̸̨̨̧̨̡̧̨͙̞̫̮͖̼͇̘͖͔̘͙̲͌̋̈́̀͜o̶̰̘͙̼̰̙̗̬̙͔̭̲̰͓̩̩̊̄̀̄̎̑͒́̔̃̀̐͋̈́̉͘͜f̸̛̛͎̱̞̣̖̼̺̟͓͖̱̭̖͔̭̙̩̲̾̇̍̒̔̐̅͜ͅ ̶̡̢̲̠̩̠̯̭̭̬̦̩̥̦̯̰̦̃̀͋͆̎͊̽̊͊̅̏̔̅̀̂͆̕͝͠͝ͅd̵͇̩̞̥̹̀̓͂͌̽̏͜ė̶͉̩̪̜͔̝̟̪̻̼̟̌̈͜͠ͅͅa̸̛̺̲̻̭̭͔̾̓͗̾͒̀̐͋ͅţ̴̛̝̰̔̎̋̊͊̅̑̌̑̿͛͂̚͘͝͝͝͝͝ḣ̵̡̡̧̺͙̮͇̟̳̼͕̝̰̖̜͎̫̣̭͎̈́̕͝.̸̨͈̿͛͂̽͋͜ͅ ̸̢̞̤̖̦͎͙͚̊̀̿͑̀̆̎̉͘͝ͅṠ̸̰̥̱̤̤̣͉̱͋̂ȯ̶̡̧̨͎̳̣̼͚̲̙̮̹̯̬̳̰͉̹͔̖̅̀̍̓̏̒͘ ̷̢̠̩̰̥̙͙̠̰̘͎͓̐̒ͅw̵̢̨̞̞͕͔̯̞̠̺̦̜͈̫̣̹̼̝̗͂̈́́̈́̌͗̂̉̈́̐̄̑̐̿͘͠è̵̬͙̖͍̲͕́͘͜ ̸̨̣͉͎̙̗͙̯̗͖̮̮̼͕͈̍́̂̐̓̀̓̋̂͜w̶̧̧̺͖̰̮̹͓̲͔̥̟̼͗́̈͊̀̈̽̿͒̕̕͠ͅi̵̛̞͂̎͆̐̈́̇̓̍͒̀̏́͆̌͌͘͜͝͝͝l̷̨̢̡̨̡̗̖̞̮̹͖͇͚̯̲̉͒̒̚͜ͅͅl̴̙̩̇͛͌̃̆̅͗͋́̈́̏͂͋̅̎͂̆͝͠͝ͅ ̶̢̢̣͔̟͚͓̖͙̱̪̘̫͇̪̙̱̦̰̻͒͋̀̔͊̌͝͠͝͝l̷̢̥͕̻̹̯̝̙̘̥͙̺̟͈̻͌͆̔͛̉̓̀̚͘ĩ̴̦̩̪̜͙̟͙̮̍͌́͆̀̆̕v̶̧̺̟͕̆̃ȩ̸̛̛̅͊͆̽͂̓̐̆͝ ̸̢̝̪̪̥̼̺̦̯̖̫͉̮͔̰͍͚͎͔̳͗͒f̶̡͛̚ơ̵̗̱̳̖͖̎̂̅͌̍̕r̵̝͚͓̹̦͐͋͛̀͒̄̋̑͗͒́̔̐̒̋͘ȩ̶̧̢̳̫̹͕̭͍̖̗̳̼̜̙̞͈̀̅͊͝͝ͅv̵̨͇͙̩̖͉͚͈̈̐̃ȩ̵̪͉͍̯̳̤̯͔͕͇̖̖͆̔͛́̂̎̾̓̂̅̎͆̑̚͘͘͜r̵̫̝͇̻̘̯̘̞̻̮̦̪̣̹̠̝̤͈̖̳̾.̸̢̡̖̟̬̱̼̹̬͈̗̠̙̉͗̅͆̔̅̈́\"̵̢̨͚̱͉̦͖͈̯̗͔͇̲̣̈̂̔͗̊̐͝"
    },
    {
      "name": "Helping Hand",
      "tags": "",
      "id": "38",
	  "knowledge": 1,
	  "corruption": 1,
      "text": "As you approach the librarian, you are able to make them out in better detail. The librarian has wing like mebranes wrapped around themself to form a kind of cloak. They walk on four spine like legs that extend out from under them. No arms or tendrils come out from their cloak, so they must be using their mind to move about the books. \n\nYou call out the the librarian. They turn their head, revealing their compound eyes. You ask if the librarian could use any help, but they cut you off. They thank you for your concern, but they assure you that this is their responsibility and you have no reason to be involved. They say that the library will survive but they do appologize as the books in this room are unable to be read. They complain about ruffians and tyrants before returning to their work.\n\n[[LEAVE|Book Room #2]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "Book Room #2",
          "original": "[[LEAVE|Book Room #2]]"
        }
      ],
      "hooks": [],
      "cleanText": "As you approach the librarian, you are able to make them out in better detail. The librarian has wing like mebranes wrapped around themself to form a kind of cloak. They walk on four spine like legs that extend out from under them. No arms or tendrils come out from their cloak, so they must be using their mind to move about the books. \n\nYou call out the the librarian. They turn their head, revealing their compound eyes. You ask if the librarian could use any help, but they cut you off. They thank you for your concern, but they assure you that this is their responsibility and you have no reason to be involved. They say that the library will survive but they do appologize as the books in this room are unable to be read. They complain about ruffians and tyrants before returning to their work."
    },
    {
      "name": "Interesting Book",
      "tags": "",
      "id": "39",
	  "knowledge": 1,
	  "corruption": 1,
      "text": "You take the time to look around the room, and you find a very interesting book. Tucked away behind other books you find the tome titled \"The Burning King.\"\n\n[[READ|The Burning King]]\n[[LEAVE|West Hallway]]",
      "links": [
        {
          "linkText": "READ",
          "passageName": "The Burning King",
          "original": "[[READ|The Burning King]]"
        },
        {
          "linkText": "LEAVE",
          "passageName": "West Hallway",
          "original": "[[LEAVE|West Hallway]]"
        }
      ],
      "hooks": [],
      "cleanText": "You take the time to look around the room, and you find a very interesting book. Tucked away behind other books you find the tome titled \"The Burning King.\""
    },
    {
      "name": "The Burning King",
      "tags": "",
      "id": "40",
	  "knowledge": 5,
	  "corruption": 5,
      "text": "You rest in the chair and open the book and begin to read. \n\n\"Long ago, there was a great emporer. A massive monster who towered over the world. They were so powerful that they gave light to the entire world. Their dominance over the world was so undesputed that they taunted all below them by hanging high in the sky. Their presence dominated every waking second of those below them. So tight was their grip on the world, that as they circled the world, they held a mirror in the sky to keep their presence known. Across from them was another monster, one who was a reflection of the first. The most powerful homonculus to ever exist. They shined a reflection of the light down on the parts of the world that could not see their master.\"\n\n[[CONTINUE|Entaptured]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "Entaptured",
          "original": "[[CONTINUE|Entaptured]]"
        }
      ],
      "hooks": [],
      "cleanText": "You rest in the chair and open the book and begin to read. \n\n\"Long ago, there was a great emporer. A massive monster who towered over the world. They were so powerful that they gave light to the entire world. Their dominance over the world was so undesputed that they taunted all below them by hanging high in the sky. Their presence dominated every waking second of those below them. So tight was their grip on the world, that as they circled the world, they held a mirror in the sky to keep their presence known. Across from them was another monster, one who was a reflection of the first. The most powerful homonculus to ever exist. They shined a reflection of the light down on the parts of the world that could not see their master.\""
    },
    {
      "name": "Entaptured",
      "tags": "",
      "id": "41",
	  "knowledge": 10,
	  "corruption": 10,
      "text": "The text had merely peaked your intrest, but now you must know. No other tomes spoke of The Burning King. You could not find mention of him anywhere. He was no were to be seen within the countless tomes of this room. So you left, you ventured out into the library to find more, but again to no avail. You continued searching. Looking as far as you could but you could not find more. You could not leave the library now, not when you had more to find. You had to research this creature. Find more that there is to know about The Burning King. You continue to search...\n\n[[END|The End]]",
      "links": [
        {
          "linkText": "END",
          "passageName": "The End",
          "original": "[[END|The End]]"
        }
      ],
      "hooks": [],
      "cleanText": "The text had merely peaked your intrest, but now you must know. No other tomes spoke of The Burning King. You could not find mention of him anywhere. He was no were to be seen within the countless tomes of this room. So you left, you ventured out into the library to find more, but again to no avail. You continued searching. Looking as far as you could but you could not find more. You could not leave the library now, not when you had more to find. You had to research this creature. Find more that there is to know about The Burning King. You continue to search..."
    }
  ]
}

def find_current_location(location_label):
	if "passages" in world:
		for passage in world["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}

# ----------------------------------------------------------------

def render(current_location, knowledge, corruption, moves):
	if "name" in current_location and "cleanText" in current_location:
		print("You are at the " + str(current_location["name"]))
		print(current_location["cleanText"] + "\n")
	options = current_location["links"]
	print("Knowledge:" + str(knowledge))
	print("Corruption:" + str(corruption))
	print("Moves: " + str(moves))
	for i in options:
		for j in i:
			if j == "linkText":
				k = i[j]
				print(k)


def get_input():
	response = input("What do you want to do? ")
	response = response.upper().strip()
	return response

def update(current_location, location_label, response):
	if response == "":
		return location_label
	if "links" in current_location:
		for link in current_location["links"]:
			if link["linkText"] == response:
				return link["passageName"]
	print("I don't understand what you are trying to do. Try again.")
	return location_label


# ----------------------------------------------------------------

location_label = "The Maw of Knowledge"
current_location = {}
response = ""
knowledge = 0
corruption = 0
moves = 0

while True:
	if response == "QUIT":
		break
	location_label = update(current_location, location_label, response)
	current_location = find_current_location(location_label)
	render(current_location, knowledge, corruption, moves)
	response = get_input()
	knowledge = knowledge + current_location["knowledge"]
	corruption = corruption + current_location["corruption"]
	moves += 1
	

	



print("Thanks for playing!")