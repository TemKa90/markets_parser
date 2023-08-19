import requests
import pandas as pd
skinList = pd.DataFrame(columns=['name'])
start = 0
while(True):
    URL = f"https://steamcommunity.com/market/search/render/?search_descriptions=0&sort_column=name&sort_dir=desc&appid=730&norender=1&start={start}&count=100&category_730_ItemSet[]=any&category_730_ProPlayer[]=any&category_730_StickerCapsule[]=any&category_730_TournamentTeam[]=any&category_730_Weapon[]=any&category_730_Rarity[]=tag_Rarity_Mythical_Weapon&category_730_Rarity[]=tag_Rarity_Legendary_Weapon&category_730_Rarity[]=tag_Rarity_Ancient_Weapon&category_730_Rarity[]=tag_Rarity_Contraband&category_730_Type[]=tag_CSGO_Type_Pistol&category_730_Type[]=tag_CSGO_Type_SMG&category_730_Type[]=tag_CSGO_Type_Rifle&category_730_Type[]=tag_CSGO_Type_Shotgun&category_730_Type[]=tag_CSGO_Type_SniperRifle&category_730_Type[]=tag_CSGO_Type_Machinegun&category_730_Type[]=tag_CSGO_Type_Knife&category_730_Type[]=tag_Type_Hands&appid=730"
    #"https://steamcommunity.com/market/search/render/?search_descriptions=0&sort_column=name&sort_dir=desc&appid=252490&norender=1&start={start}&count=100" Для раста

    r = requests.get(URL)
    data = r.json()
    try:
        df_temp = pd.DataFrame([i['name'] for i in data['results']],columns=['name'])
        skinList = pd.concat([skinList, df_temp], ignore_index=True)
        if(df_temp.size % 100 == 0): #if number is not 100, then its the last results.
            start += 100
        else:
            break
    except TypeError: 
        skinList.to_csv('csv/list.csv', index=False, header=False)
        print("error here at " + str(start))
        break
skinList.to_csv('csv/list.csv', index=False, header=False)