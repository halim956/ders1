while True:
  meme_dict = {
              "CRINGE": "Garip ya da utandırıcı bir şey",
              "LOL": "Komik bir şeye verilen cevap",
              "DM":"direct mesaj",
              "FPS":"saniyedeki kare hızı",
              "ROFL":"bir şakaya karşılık cevap",
              "SHEESH":"onaylamak",
              "CREEPY":"korkunç",
              "AGGRO":"sinirlenme/agresiflik",
              }
  print("________________________________________________________________")
  word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
  if word in meme_dict.keys():
      print(meme_dict[word])  
  else:
    print("sözlükte böyle bir kelime bulanamadım :( ")
    
