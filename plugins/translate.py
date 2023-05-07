from googletrans import Translator
from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup
)




from helper.database import find , insert
from helper.list import list

@Client.on_message(filters.private & filters.command(['start']))
async def start(client, message):
          insert(int(message.chat.id))
          await message.reply_text(text =f"**Hello 👋🏻 {message.from_user.first_name} ❤️\n\nI'm Star Bots Official Google Translator Bot. I Can Translate any Language to You Selected Language. You Can Set Your Language Permanently.\n\nTo know How to Use me check /help.\n\nI'll Work in Groups and Also Inline Anywhere.**",reply_to_message_id = message.message_id , parse_mode="markdown", reply_markup=InlineKeyboardMarkup(            [                [                    InlineKeyboardButton("🤖 Bot Channel" ,url="https://t.me/Star_Bots_Tamil"),InlineKeyboardButton("Go Inline Here", switch_inline_query_current_chat=query) ],                 [InlineKeyboardButton("🎥 Movie Updates", url="https://t.me/Star_Moviess_Tamil"),InlineKeyboardButton("👥 Support Group",url = "https://t.me/Star_Bots_Tamil_Support") ]           ]        ) )
  
@Client.on_message(filters.private & filters.command(['help']))
async def help(client, message):
          insert(int(message.chat.id))
          await message.reply_text(text =f"**Hey 👋🏻 {message.from_user.first_name} Follow These Steps :-\n\n● Send /set language_name\n● Send /unset for Unsetting Current Default Language\n● Send /list for Languages List\n● Just Send a Text for Translation\n● Reply with Any Text With /translate language_name (Support Only Groups)\n● /text2speech - Reply with Text to Get Audio Speech 💬\n\nAvailable Commands\n\n● /start - Check if 😊 I'm Alive\n● /help - How to Use❓\n● /about - to Know About Me 😌\n\nMade by [Star Bots Tamil](https://t.me/Star_Bots_Tamil)**",reply_to_message_id = message.message_id , parse_mode="markdown", reply_markup=InlineKeyboardMarkup(            [                [                    InlineKeyboardButton("🤖 Bot Channel" ,switch_inline_query_current_chat=query) ],                 [InlineKeyboardButton("🎥 Movie Updates", url="https://t.me/Star_Moviess_Tamil"),InlineKeyboardButton("👥 Support Group",url = "https://t.me/Star_Bots_Tamil_Support") ]           ]        ) )

@Client.on_message(filters.private & filters.command(['about']))
async def about(client, message):
          insert(int(message.chat.id))

          await message.reply_text(text =f"**🤖 My Name :- [Google Translator Star Bots](https://t.me/Google_Translator_Star_Bot)\n\n🧑🏻‍💻 Developer :- [Karthik](https://t.me/TG_Karthik)\n\n📝 Language :- Python3\n\n📚 Framework :- Pyrogram\n\n📡 Hosted on :- VPS\n\n🤖 Bot Channel :- [Star Bots Tamil](https://t.me/Star_Bots_Tamil)\n\n🎥 Movie Updates :- [Star Movies Tamil](https://t.me/Star_Moviess_Tamil)**",reply_to_message_id = message.message_id , parse_mode="markdown", reply_markup=InlineKeyboardMarkup(            [                [                    InlineKeyboardButton("🤖 Bot Channel" ,url="https://t.me/Star_Bots_Tamil") ],                 [InlineKeyboardButton("🎥 Movie Updates", url="https://t.me/Star_Moviess_Tamil"),InlineKeyboardButton("👥 Support Group",url = "https://t.me/Star_Bots_Tamil_Support") ]           ]        ) )

@Client.on_message(filters.private & filters.command(['list']))
async def list(client, message):
          insert(int(message.chat.id))
          await message.reply_text(text =f"**List is in The Form\nLanguage Code -> Language\n\nta -> தமிழ் -> Tamil\naf -> Afrikaans\nsq -> Albanian\nam -> Amharic\nar -> Arabic\nhy -> Armenian\naz -> Azerbaijani\neu -> Basque\nbe -> Belarusian\nbn -> Bengali\nbs -> Bosnian\nbg -> Bulgarian\nca -> Catalan\nceb -> Cebuano\nny -> Chichewa\nzh-cn -> Chinese\nco -> Corsican\nhr -> Croatian\ncs -> Czech\nda -> Danish\nnl -> Dutch\nen -> English\neo -> Esperanto\net -> Estonian\ntl -> Filipino\nfi -> Finnish\nfr -> French\nfy -> Frisian\ngl -> Galician\nka -> Georgian\nde -> German\nel -> Greek\ngu -> Gujarati\nht -> Haitian creole\nha -> Hausa\nhaw -> Hawaiian\niw -> Hebrew\nhi -> Hindi\nhmn -> Hmong\nhu -> Hungarian\nis -> Icelandic\nig -> Igbo\nid -> Indonesian\nga -> Irish\nit -> Italian\nja -> Japanese\njw -> Javanese\nkn -> Kannada\nkk -> Kazakh\nkm -> Khmer\nrw -> Kinyarwanda\nko -> Korean\nku -> Kurdish (kurmanji)\nky -> Kyrgyz\nlo -> Lao\nla -> Latin\nlv -> Latvian\nlt -> Lithuanian\nlb -> Luxembourgish\nmk -> Macedonian\nmg -> Malagasy\nms -> Malay\nml -> Malayalam\nmt -> Maltese\nmi -> Maori\nmr -> Marathi\nmn -> Mongolian\nmy -> Myanmar (burmese)\nne -> Nepali\nno -> Norwegian\nor -> Oriya\nps -> Pashto\nfa -> Persian\npl -> Polish\npt -> Portuguese\npa -> Punjabi\nro -> Romanian\nru -> Russian\nsm -> Samoan\ngd -> Scots gaelic\nsr -> Serbian\nst -> Sesotho\nsn -> Shona\nsd -> Sindhi\nsi -> Sinhala\nsk -> Slovak\nsl -> Slovenian\nso -> Somali\nes -> Spanish\nsu -> Sundanese\nsw -> Swahili\nsv -> Swedish\ntg -> Tajik\nta -> Tamil\ntt -> Tatar\nte -> Telugu\nth -> Thai\ntr -> Turkish\ntk -> Turkmen\nug -> Uighur\nuk -> Ukrainian\nur -> Urdu\nuz -> Uzbek\nvi -> Vietnamese\ncy -> Welsh\nxh -> Xhosa\nyi -> Yiddish\nyo -> Yoruba\nzu -> Zulu**",reply_to_message_id = message.message_id , parse_mode="markdown", reply_markup=InlineKeyboardMarkup(            [                [                    InlineKeyboardButton("🤖 Bot Channel" ,url="https://t.me/Star_Bots_Tamil") ],                 [InlineKeyboardButton("🎥 Movie Updates", url="https://t.me/Star_Moviess_Tamil"),InlineKeyboardButton("👥 Support Group",url = "https://t.me/Star_Bots_Tamil_Support") ]           ]        ) )


            
@Client.on_message(filters.private & filters.text  )
async def echo(client, message):
	keybord1= InlineKeyboardMarkup( [
        [InlineKeyboardButton("தமிழ் -> Tamil",callback_data = "ta")
	],
        [ 
            InlineKeyboardButton("Afrikaans", callback_data='af'),
             InlineKeyboardButton("Albanian", callback_data='sq'),
            InlineKeyboardButton("Amharic",callback_data ='am'),
        ],
        [   InlineKeyboardButton("Arabic", callback_data='ar'),
        InlineKeyboardButton("Armenian", callback_data='hy'),      
        InlineKeyboardButton("Azerbaijani",callback_data = 'az'),        
        ],
        [InlineKeyboardButton("Basque",callback_data ="eu"),
        	 InlineKeyboardButton("Belarusian",callback_data ="be"),       	
	InlineKeyboardButton("Bengali",callback_data="bn")],
	
	[InlineKeyboardButton("Bosnian",callback_data = "bs"),
	InlineKeyboardButton("Bulgarian",callback_data ="bg"),
	InlineKeyboardButton("Catalan",callback_data = "ca")
	],
	[ 
	InlineKeyboardButton("Corsican",callback_data ="co"),
	InlineKeyboardButton("Croatian",callback_data = "hr"),
	InlineKeyboardButton("Czech", callback_data = "cs"),
	],
	[ InlineKeyboardButton("Danish",callback_data = "da"),
	InlineKeyboardButton("Dutch",callback_data = "nl"),
	InlineKeyboardButton("Esperanto",callback_data = "eo"),	 
	],
	[InlineKeyboardButton(" Next --->",callback_data = "page2")
	]
	] )
	try:
		code =find(int(message.chat.id))
	except Exception as e:
		await message.reply_text(f" Error : {e}\nclick /start ........")
		return 
		
	if code :
			try:
				translator = Translator()
				translation = translator.translate(message.text,dest = code)
			except Exception as e:
				await message.reply_text(f"Error : {e}")
				return
			try:
					for i in list:
						if list[i]==translation.src:
							fromt = i
						if list[i] == translation.dest:
							to = i
					await message.reply_text(f"Translated from **{fromt.capitalize()}** To **{to.capitalize()}**\n\n```{translation.text}```\n\n join @lntechnical")
			except Exception as e:
					await message.reply_text(f"Translated from **{translation.src}** To **{translation.dest}**\n\n```{translation.text}```\n\n join @lntechnical")
	else:
		await  message.reply_text("**Select Language 👇🏻**",reply_to_message_id = message.message_id, reply_markup =keybord1)

@Client.on_callback_query()
async def translate_text(bot,update):
      keybord1= InlineKeyboardMarkup( [
        [InlineKeyboardButton("தமிழ் -> Tamil",callback_data = "ta")
	 ],
        [ 
            InlineKeyboardButton("Afrikaans", callback_data='af'),
             InlineKeyboardButton("Albanian", callback_data='sq'),
            InlineKeyboardButton("Amharic",callback_data ='am'),
        ],
        [   InlineKeyboardButton("Arabic", callback_data='ar'),
        InlineKeyboardButton("Armenian", callback_data='hy'),      
        InlineKeyboardButton("Azerbaijani",callback_data = 'az'),        
        ],
        [InlineKeyboardButton("Basque",callback_data ="eu"),
        	 InlineKeyboardButton("Belarusian",callback_data ="be"),       	
	InlineKeyboardButton("Bengali",callback_data="bn")],
	
	[InlineKeyboardButton("Bosnian",callback_data = "bs"),
	InlineKeyboardButton("Bulgarian",callback_data ="bg"),
	InlineKeyboardButton("Catalan",callback_data = "ca")
	],
	[ 
	InlineKeyboardButton("Corsican",callback_data ="co"),
	InlineKeyboardButton("Croatian",callback_data = "hr"),
	InlineKeyboardButton("Czech", callback_data = "cs"),
	],
	[ InlineKeyboardButton("Danish",callback_data = "da"),
	InlineKeyboardButton("Dutch",callback_data = "nl"),
	InlineKeyboardButton("Esperanto",callback_data = "eo"),	 
	],
	[InlineKeyboardButton(" Next --->",callback_data = "page2")
	]
	] )

      keybord2= InlineKeyboardMarkup([
           [InlineKeyboardButton("English",callback_data = "en"),
           InlineKeyboardButton("Estonian",callback_data = "et"),
           InlineKeyboardButton("Finnish",callback_data = "fi")
           ],
           [InlineKeyboardButton("French",callback_data = "fr"),
           InlineKeyboardButton("Frisian",callback_data = "fy"),
           InlineKeyboardButton("Galician",callback_data = "gl")
           ],
           [InlineKeyboardButton("Georgian",callback_data = "ka"),
           InlineKeyboardButton("German",callback_data = "de"),
           InlineKeyboardButton("Greek",callback_data = "el")
           ],
           [InlineKeyboardButton("Gujarati",callback_data = "gu"),
           InlineKeyboardButton("Haitian Creole",callback_data = "ht"),
           InlineKeyboardButton("Hausa",callback_data ="ha")
           ],
           [InlineKeyboardButton("Hindi",callback_data = "hi"),
           InlineKeyboardButton("Hungarian",callback_data = "hu"),
           InlineKeyboardButton("Icelandic",callback_data = "is")
           ],
           [InlineKeyboardButton("Igbo",callback_data = "ig"),
           InlineKeyboardButton("Indonesian",callback_data = "id"),
           InlineKeyboardButton("Irish",callback_data = "ga")
           ],
           [InlineKeyboardButton("<--- Back",callback_data = "page1"),
           InlineKeyboardButton(" Next --->",callback_data = "page3"),
           ]
            ])
		
      keybord3 = InlineKeyboardMarkup([
                [ InlineKeyboardButton("Italian",callback_data = "it"),
                InlineKeyboardButton("Japanese",callback_data = "ja"),
                InlineKeyboardButton("Javanese",callback_data = "jv")
                ],
                [InlineKeyboardButton("Kannada",callback_data = "kn"),
                InlineKeyboardButton("Kazakh",callback_data = "kk"),
                InlineKeyboardButton("Khmer",callback_data = "km")
                ],
                [InlineKeyboardButton("Kinyarwanda",callback_data = "rw"),
                InlineKeyboardButton("Korean",callback_data ="ko"),
                InlineKeyboardButton("Kurdish",callback_data = "ku")
                ],
                [ InlineKeyboardButton("Kyrgyz",callback_data ="ky"),
                InlineKeyboardButton("Lao",callback_data = "lo"),
                InlineKeyboardButton("Latin",callback_data = "la")
                ],
                [InlineKeyboardButton("Latvian",callback_data = "lv"),
                InlineKeyboardButton('Lithuanian',callback_data ="lt"),
                InlineKeyboardButton("Luxembourgish",callback_data = "lb")
                ],
                [InlineKeyboardButton("Macedonian",callback_data = "mk"),
                InlineKeyboardButton("Malagasy",callback_data ="mg"),
                InlineKeyboardButton("Malay",callback_data ="ms")
                ],
                [InlineKeyboardButton("<--- Back",callback_data = "page2"),
                InlineKeyboardButton(" Next --->",callback_data = "page4")
                ]
              
 
 ])

      keybord4 = InlineKeyboardMarkup([
          [InlineKeyboardButton("Malayalam",callback_data = "ml"),
          InlineKeyboardButton("Maltese",callback_data = "mt"),
          InlineKeyboardButton("Maori",callback_data = "mi")
          ],
          [InlineKeyboardButton("Marathi",callback_data = "mr"),
          InlineKeyboardButton("Mongolian",callback_data = "mn"),
          InlineKeyboardButton("Myanmar (Burmese)",callback_data = "my")
          ],
          [InlineKeyboardButton("Nepali",callback_data ="ne"),
          InlineKeyboardButton("Norwegian",callback_data = "no"),
          InlineKeyboardButton("Nyanja (Chichewa)",callback_data = "ny")
          ],
          [InlineKeyboardButton("Odia",callback_data = "or"),
          InlineKeyboardButton("Pashto",callback_data = "ps"),
          InlineKeyboardButton("Persian",callback_data = "fa"),
          ],
          [InlineKeyboardButton("Polish",callback_data = "pl"),
          InlineKeyboardButton("Portuguese",callback_data = "pt"),
          InlineKeyboardButton("Punjabi",callback_data = "pa"),
          ],
          [InlineKeyboardButton("Romanian",callback_data = "ro"),
          InlineKeyboardButton("Russian",callback_data = "ru"),
          InlineKeyboardButton("Samoan",callback_data= "sm"),
          ],
          [InlineKeyboardButton("<--- Back",callback_data = "page3"),
          InlineKeyboardButton("Next --->",callback_data = "page5")
          ]
          
 
 
 
 ])

      keybord5 = InlineKeyboardMarkup([
         [InlineKeyboardButton("Scots Gaelic",callback_data = "gd"),
         InlineKeyboardButton("Serbian",callback_data = "sr"),
         InlineKeyboardButton("Sesotho",callback_data = "st")
         ],
         [InlineKeyboardButton("Shona",callback_data ="sn"),
         InlineKeyboardButton("Sindhi",callback_data ="sd"),
         InlineKeyboardButton("Sinhala (Sinhalese)",callback_data = "si")
         ],
         [InlineKeyboardButton("Slovak",callback_data = "sk"),
         InlineKeyboardButton("Slovenian",callback_data = "sl"),
         InlineKeyboardButton("Somali",callback_data = "so")
         ],
         [InlineKeyboardButton("Spanish",callback_data = "es"),
         InlineKeyboardButton("Sundanese",callback_data ="su"),
         InlineKeyboardButton("Swahili",callback_data ="sw")
         ],
         [InlineKeyboardButton("Swedish",callback_data = "sv"),
         InlineKeyboardButton("Tagalog (Filipino)",callback_data ='tl'),
         InlineKeyboardButton("Tajik",callback_data = "tg")
         ],
         [InlineKeyboardButton("Tamil",callback_data = "ta"),
         InlineKeyboardButton("Tatar",callback_data = "tt"),
         InlineKeyboardButton("Telugu",callback_data = "te")
         ],
         [InlineKeyboardButton("<--- Back",callback_data = "page4"),
         InlineKeyboardButton("Next --->",callback_data = "page6")
         ]  ])




      keybord6 =  InlineKeyboardMarkup([
       [InlineKeyboardButton("Thai",callback_data = "th"),
       InlineKeyboardButton("Turkish",callback_data = "tr"),
       InlineKeyboardButton("!Not Valid",callback_data ="en")     
       ],
       [InlineKeyboardButton("Ukrainian",callback_data = "uk"),
       InlineKeyboardButton("Urdu",callback_data = "ur"),
       InlineKeyboardButton("Uyghur",callback_data ="ug")
       
       ],
       [InlineKeyboardButton("Uzbek",callback_data = "uz"),
       InlineKeyboardButton("Vietnamese",callback_data ="vi"),
       InlineKeyboardButton("Welsh",callback_data = "cy")
       
       ],
       [InlineKeyboardButton("Xhosa",callback_data = "xh"),
       InlineKeyboardButton("Yiddish",callback_data = "yi"),
       InlineKeyboardButton("Yoruba",callback_data = "yo")],
       [InlineKeyboardButton("<--- Back",callback_data = "page5")
       
       ] ])
      
      
      
      tr_text = update.message.reply_to_message.text
      cb_data = update.data
      if cb_data== "page2":
      	await update.message.edit("**Select Language 👇🏻**",reply_markup = keybord2)
      elif cb_data == "page1":
      	await update.message.edit("**Select Language 👇🏻**",reply_markup =keybord1)
      elif cb_data =="page3":
      	await update.message.edit("**Select Language 👇🏻**",reply_markup =keybord3)
      elif cb_data == "page4":
      	await update.message.edit("**Select Language 👇🏻**",reply_markup =keybord4)
      elif cb_data =="page5":
      	await update.message.edit("**Select Language 👇🏻**",reply_markup =keybord5)
      elif cb_data =="page6":
      	await update.message.edit("**Select Language 👇🏻**",reply_markup =keybord6)
      else :
      		try:
      			translator = Translator()
      			translation = translator.translate(tr_text,dest = cb_data)
      		except Exception as e:
      			await update.message.edit(f"Error : {e}")
      			return
      		try:
      			for i in list:
      				if list[i]==translation.src:
      					fromt = i
      				if list[i] == translation.dest:
      					to = i 
      			await update.message.edit(f"**Translated From {fromt.capitalize()} To {to.capitalize()}\n\n```{translation.text}```\n\nJoin [Star Bots Tamil](https://t.me/Star_Bots_Tamil)")
      		except Exception as e:
      			await update.message.edit(f"**Translated From {translation.src} To {translation.dest}\n\n```{translation.text}```\n\nJoin [Star Bots Tamil](https://t.me/Star_Bots_Tamil)")
      						
