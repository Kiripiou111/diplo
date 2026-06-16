from random import randint
import requests
import discord
from json import loads
from asyncio import sleep
import os
from keep_alive import keep_alive
from supabase import create_client, Client

#Variables Bot :
TOKEN = os.environ.get("token")

url: str = os.environ.get("url")
key: str = os.environ.get("key")
supabase: Client = create_client(url, key)

intents = discord.Intents.default()
intents.presences = True
intents.members = True
intents.message_content = True
client = discord.Client(intents=intents)

channel_id = 1167789020575711262
channel_name = "suggestions-v2-diplomacy"

admin_liste = [922077625583804426, 567122368686981133, 697918875500544091, 705115312986521681, 1192918958144241706, 1233458488332648501, 115486361833701383, 1015328595155099738, 778651161989087292]

#Mes fonctions INTERNES:
def log_error(e):
    try:
        supabase.table("logss").insert({
            "error": str(e)
        }).execute()
    except Exception as log_e:
        print("Impossible d'écrire dans les logs :", log_e)
def getdate():
    try:
        result = (
        supabase.table("Diplo")
        .select("n")
        .order("id", desc=True)
        .limit(1)
        .execute()
        )

        if result.data:
           return int(result.data[0]["n"])

        return 0

    except Exception as e:
        log_error(f"getdate : {e}")
        return  0 
def newdate(d):
    try:
        result = (
            supabase.table("Diplo").insert({"n": d}).execute()
        )
        return result

    except Exception as e:
        log_error(f"newdate({d}) : {e}") 
def delete_last_date():
    try:
        result = (
            supabase.table("Diplo")
            .select("id")
            .order("id", desc=True)
            .limit(1)
            .execute()
        )

        if result.data:
            last_id = result.data[0]["id"]

            supabase.table("Diplo") \
                .delete() \
                .eq("id", last_id) \
                .execute()


    except Exception as e:
        log_error(f"delete_last_date : {e}")
def pickNoArsenal():
    n = 0
    while n == 0:
        chosen_one = regions_terrestre[randint(0, len(regions_terrestre)-1)]
        if chosen_one not in arsenaux:
            n = 1
    return chosen_one 
def formatage(path_file): 
    obfi = open(path_file, "r")
    while 1:
        line = obfi.readline()
        if line == '':
            break
        line = line.replace('\n', '')
        line = '"' + line + '"' + ","
        print(line, end='')

#Variables programme : SP
stat_limite = 15
pays = ["Etats-Unis (Ouest)", "Inde", "Argentine", "Afrique du Sud", "Russie (Est)", "Etats-Unis (Est)", "France", "Australie", "Canada", "Russie (Ouest)", "Arabie", "Antarctique", " Vénezuela", "Brésil", "Congo", "Mali", "Egypte", "Chine"]
arsenaux = ['NT (Territoires du Nord)', 'Qu (Québec)', 'NwF Nouveau Brunswick', 'Bri (Canada)', 'Paw (USA)', 'Clf (California)', 'Un (Caroline USA)', 'FL (Floride)', 'DP (USA)', 'Ve (Venezuela)', 'Col (Colombie)', 'Eq (Equateur)', 'Sa (Brésil)', 'Bho (Brésil)', 'Rio (Brésil)', 'AN (Angleterre)', 'AL(Allemagne)', 'FR (France)', 'StP (Saint Petersbourg)', 'MO (Moscou)', 'BE (Bielorussie)', 'Sy (Syrie)', 'Iq (Iraq)', 'SAr (Arabie Saoudite)', 'Ly (Lybie)', 'Eg (Egypte)', 'So (Soudan)', 'Mal (Mali)', 'Gh (Ghana)', 'Gui (Guinée)', 'Zai (Zaïre)', 'Tan (Tanzanie)', 'Nen (Kenya)', 'Chi (Chili)', 'Arg (Argentine)', 'Bua (Buenos Aires)', 'Nam (Namibie)', 'SuA (Afrique du Sud)', 'San (Antarctique)', 'Maw (Antarctique)', 'Vos (Antarctique)', 'Cat (Antarctique)', 'WA (Ouest Australie)', 'Vic (Victoria Australie)', 'Qsl (Queesland Australie)', 'MU (Mumbay)', 'CA (Calcutta)', 'DE (Delhi)', 'GU (Guanxi)', 'SH (Shangaï)', 'BEI (Beijing)', 'MON (Mongolie)', 'IRK (Russie)', 'YA (Yakoutie Russie)', 'God (Groenland)', 'Ala (Alaska)', 'Man (Canada)', 'Gl (Grands Lacs USA)', 'MdW (Midwest)', 'Mex (Mexique)', 'Gal (Galapagos)', 'Ama (Amazonie)', 'Bra (Brésil)', 'Re (Récif Brésil)', 'Bol (Bolivie)', 'Ur (Uruguay)', 'Bat (Antarctique)', 'PS (Pôle Sud)', 'Syo (Antarctique)', 'Zim (Zimbabwe)', 'Moz (Mozambique)', 'Con (Congo)', 'Ug (Ouganda)', 'Cam (Cameroun)', 'Et (Ethiopie)', 'Cha (Tchad)', 'Ma (Maroc)', 'It (Italie)', 'SC (Scandinavie)', 'UK (Ukraine)', 'TU (Turquie)', 'AR (Arménie)', 'WS (Russie)', 'AF (Afghanistan)', 'ES (Russie)', 'BA (Bangladesh)', 'TH (Thaïlande)', 'LA (Laos)', 'VLC (Vladivostok Russie)', 'JA (Japon)', 'IN (Indonésie)', 'NZ (Nouvelle-Zélande)']
regions_terrestre = ['Haw (Hawaï)', 'Yuk ( Canada)', 'Alb (Canada)', 'Sas (Canada)', 'Ont (Canada)', 'Ne (New-York)', 'Thu (Groenland)', 'Tex (Texas)', 'Mon (Mexique)', 'Cu (Cuba)', 'Pa (Panama)', 'Guy (Guyane)', 'Pé (Pérou)', 'SaP (Sao Paolo)', 'Men (Argentine)', 'MBL (Antarctique)', 'Ape (Antarctique)', 'Nov (Antarctique)', 'ND (Antarctique)', 'Dud (Antarctique)', 'Len (Antarctique)', 'Ris (Antarctique)', 'Sau (Australie)', 'Nsw (Australie)', 'NTe (Australie)', 'PH (Philippines) ', 'VI (Vietnam)', 'BU (Birmanie)', 'KO (Corée)', 'HE (Hebei)', 'KAM (Kamtchatka)', 'IM (Mongolie Intérieure)', 'QI (Qinghai)', 'TI (Tibet)', 'WC (Xinjiang)', 'PA (Pakistan)', 'KY (Kirghizstan)', 'OM (Russie)', 'KA (Kazakhstan)', 'IR (Iran)', 'BS (Pays Baltes)', 'PO (Pologne)', 'BA (Balkans)', 'AH (Autriche-Hongrie)', 'SP (Espagne)', 'Alg (Algérie)', 'Mau (Mauritanie)', 'Ni (Niger)', 'Nge (Nigéria)', 'CAR (Centrafrique)', 'SuS (Soudan du Sud)', 'Som (Somalie)', 'Ang (Angola)', 'Zam (Zambie)', 'Bot (Botswana) (', 'Mad (Madagascar)', 'NT (Territoires du Nord)', 'Qu (Québec)', 'NwF Nouveau Brunswick', 'Bri (Canada)', 'Paw (USA)', 'Clf (California)', 'Un (Caroline USA)', 'FL (Floride)', 'DP (USA)', 'Ve (Venezuela)', 'Col (Colombie)', 'Eq (Equateur)', 'Sa (Brésil)', 'Bho (Brésil)', 'Rio (Brésil)', 'AN (Angleterre)', 'AL(Allemagne)', 'FR (France)', 'StP (Saint Petersbourg)', 'MO (Moscou)', 'BE (Bielorussie)', 'Sy (Syrie)', 'Iq (Iraq)', 'SAr (Arabie Saoudite)', 'Ly (Lybie)', 'Eg (Egypte)', 'So (Soudan)', 'Mal (Mali)', 'Gh (Ghana)', 'Gui (Guinée)', 'Zai (Zaïre)', 'Tan (Tanzanie)', 'Nen (Kenya)', 'Chi (Chili)', 'Arg (Argentine)', 'Bua (Buenos Aires)', 'Nam (Namibie)', 'SuA (Afrique du Sud)', 'San (Antarctique)', 'Maw (Antarctique)', 'Vos (Antarctique)', 'Cat (Antarctique)', 'WA (Ouest Australie)', 'Vic (Victoria Australie)', 'Qsl (Queesland Australie)', 'MU (Mumbay)', 'CA (Calcutta)', 'DE (Delhi)', 'GU (Guanxi)', 'SH (Shangaï)', 'BEI (Beijing)', 'MON (Mongolie)', 'IRK (Russie)', 'YA (Yakoutie Russie)', 'God (Groenland)', 'Ala (Alaska)', 'Man (Canada)', 'Gl (Grands Lacs USA)', 'MdW (Midwest)', 'Mex (Mexique)', 'Gal (Galapagos)', 'Ama (Amazonie)', 'Bra (Brésil)', 'Re (Récif Brésil)', 'Bol (Bolivie)', 'Ur (Uruguay)', 'Bat (Antarctique)', 'PS (Pôle Sud)', 'Syo (Antarctique)', 'Zim (Zimbabwe)', 'Moz (Mozambique)', 'Con (Congo)', 'Ug (Ouganda)', 'Cam (Cameroun)', 'Et (Ethiopie)', 'Cha (Tchad)', 'Ma (Maroc)', 'It (Italie)', 'SC (Scandinavie)', 'UK (Ukraine)', 'TU (Turquie)', 'AR (Arménie)', 'WS (Russie)', 'AF (Afghanistan)', 'ES (Russie)', 'BA (Bangladesh)', 'TH (Thaïlande)', 'LA (Laos)', 'VLC (Vladivostok Russie)', 'JA (Japon)', 'IN (Indonésie)', 'NZ (Nouvelle-Zélande)']
regions_ter_vides = ['Haw (Hawaï)', 'Yuk ( Canada)', 'Alb (Canada)', 'Sas (Canada)', 'Ont (Canada)', 'Ne (New-York)', 'Thu (Groenland)', 'Tex (Texas)', 'Mon (Mexique)', 'Cu (Cuba)', 'Pa (Panama)', 'Guy (Guyane)', 'Pé (Pérou)', 'SaP (Sao Paolo)', 'Men (Argentine)', 'MBL (Antarctique)', 'Ape (Antarctique)', 'Nov (Antarctique)', 'ND (Antarctique)', 'Dud (Antarctique)', 'Len (Antarctique)', 'Ris (Antarctique)', 'Sau (Australie)', 'Nsw (Australie)', 'NTe (Australie)', 'PH (Philippines) ', 'VI (Vietnam)', 'BU (Birmanie)', 'KO (Corée)', 'HE (Hebei)', 'KAM (Kamtchatka)', 'IM (Mongolie Intérieure)', 'QI (Qinghai)', 'TI (Tibet)', 'WC (Xinjiang)', 'PA (Pakistan)', 'KY (Kirghizstan)', 'OM (Russie)', 'KA (Kazakhstan)', 'IR (Iran)', 'BS (Pays Baltes)', 'PO (Pologne)', 'BA (Balkans)', 'AH (Autriche-Hongrie)', 'SP (Espagne)', 'Alg (Algérie)', 'Mau (Mauritanie)', 'Ni (Niger)', 'Nge (Nigéria)', 'CAR (Centrafrique)', 'SuS (Soudan du Sud)', 'Som (Somalie)', 'Ang (Angola)', 'Zam (Zambie)', 'Bot (Botswana) (', 'Mad (Madagascar)']
mers = ['Ber', 'NPa', 'Pac', 'Pis', 'Amu', 'Arc', 'GoA', 'SP', 'SuP', 'Bel', 'Sco', 'OuA', 'Cao', 'Car', 'GMe', 'SS', 'Lab', 'HuB', 'Nvn', 'Atm', 'GoG', 'EsA', 'Rii', 'Cos', 'Mch', 'Sin', 'Oin', 'MaS', 'Ein', 'UrS', 'Tas', 'Jav', 'Nin', 'Ara', 'Rou', 'Ben', 'SCh', 'Ech', 'Jap', 'Okh', 'Noi', 'Mdt', 'Cas', 'Nrd', 'Bar', 'Sib', 'BeS', 'BaS']
extremes = ['Ris', 'Amu', 'Bel', 'Sco', 'Rii', 'Cos', 'Sin', 'MaS', 'UrS', 'Arc', 'Arc', 'Bér', 'BeS', 'Bar', 'Sib']
regions = ['Haw', 'Yuk', 'Alb', 'Sas', 'Ont', 'Ne', 'Thu', 'Tex', 'Mon', 'Cu', 'Pa', 'Guy', 'Ama', 'Pé', 'SaP', 'Men', 'MBL', 'Ape', 'Nov', 'ND', 'Dud', 'Len', 'Ris', 'Sau', 'Nsw', 'NTe', 'PH', 'VI', 'BU', 'KO', 'HE', 'VLC', 'KAM', 'IM', 'QI', 'TI', 'WC', 'PA', 'KY', 'OM', 'KA', 'IR', 'BS', 'PO', 'BA', 'AH', 'SP', 'Alg', 'Mau', 'Ni', 'Nge', 'CAR', 'SuS', 'Som', 'Ang', 'Zam', 'Bot', 'Mad', 'NT', 'Qu', 'NwF', 'Bri', 'Paw', 'Clf', 'Un', 'FL', 'DP', 'Ve', 'Col', 'Eq', 'Sa', 'Bho', 'Rio', 'AN', 'AL', 'FR', 'StP', 'MO', 'BE', 'Sy', 'Iq', 'SAr', 'Ly', 'Eg', 'Sa', 'Mal', 'Gh', 'Gui', 'Zai', 'Tan', 'Nen', 'Chi', 'Arg', 'Bua', 'Nam', 'SuA', 'San', 'Maw', 'Vos', 'Cat', 'WA', 'Vic', 'Qsl', 'MU', 'CA', 'DE', 'GU', 'SH', 'BEI', 'MON', 'IRK', 'YA', 'God', 'Ala', 'Man', 'Gl', 'MdW', 'Mex', 'Gal', 'Ama', 'Bra', 'Re', 'Bol', 'Ur', 'Bat', 'PS', 'Syo', 'Zim', 'Moz', 'Con', 'Ug', 'Cam', 'Et', 'Cha', 'Ma', 'It', 'SC', 'UK', 'TU', 'AR', 'WS', 'AF', 'ES', 'BA', 'TH', 'LA', 'VL', 'JA', 'IN', 'NZ', 'Ber', 'NPa', 'Pac', 'Pis', 'Amu', 'Arc', 'GoA', 'Esp', 'SuP', 'Bel', 'Sco', 'OuA', 'Cao', 'Car', 'GMe', 'SS', 'Lab', 'HuB', 'Nvn', 'Atm', 'GoG', 'EsA', 'Rii', 'Cos', 'Mch', 'Sin', 'Oin', 'MaS', 'Ein', 'UrS', 'Tas', 'Jav', 'Nin', 'Ara', 'Ben', 'Rou', 'SCh', 'Ech', 'Jap', 'Okh', 'Noi', 'Mdt', 'Cas', 'Nrd', 'Bar', 'Sib', 'BeS', 'BaS']
an = 1900
campagnes = ["Campagne de Printemps ", "Campagne d'automne "]
n_campagne = getdate()

# Mes fonctions EXTERNES
def Nostalgie():
    global n_campagne
    date = getdate()
    newdate(date-1)
    n_campagne = date-1
def regret():
    global n_campagne
    delete_last_date()
    n_campagne = getdate()
def intro():
    txt = ""
    dico_actions_possibles = {"1" : Pb(), "2" : Miracle(), "3" : Propagande(), "4" : MerGelée(), "5" : SoutienPopulaire(), "6" : Blitzkrieg(), "7": enlisement(), "8": isolement(), "9" : Rebellion()}
    actions = ["Pb", "Miracle", "Propagande", "MerGelée", "SoutienPopulaire"]
    for i in range(1, 6):
        txt += actions[i-1] + " --> " + dico_actions_possibles[str(i)] + "\n"
    return txt  
def Pb():
    region_cible = regions[randint(0, len(regions)-1)]
    pbs = ["une epidemie ", "un volcan ", "une famine ", "un accident ", "un seisme ", "une TERRIBLE DIARRHEE "]
    pb = pbs[randint(0, len(pbs)-1)]
    retour = "Malus de defense : **" + str(region_cible) + "** subit " + str(pb) + "soit un malus de 0.5 en défense. " + "\n"
    return retour
def isolement():
    region_cible = regions[randint(0, len(regions)-1)]
    retour = "Isolement : **" + str(region_cible) + "** subit une tempete de neige ou de sable et rencontre donc un isolement complet du reste du monde, les troupes ne peuvent ni entrer ni sortir. " + "\n"
    return retour
def Rebellion(): #Trop_Cheaté
    region_cible = regions_terrestre[randint(0, len(regions_terrestre)-1)]
    retour = "Guerre Civile : **" + str(region_cible) + "** subit une guerre civile, la region s'autonomise et compte bien se defendre. Elle devient neutre et une armée blanche apparait. " + "\n"                           
    return retour  
def MerGelée():
    pot = mers + extremes
    region_cible = pot[randint(0, len(pot)-1)]
    retour = "Mer Gelée : **" + str(region_cible) + "** est traversée par une vague de froid; la mer a gelé. Les unités terrestres pourront la traverser pour la prochaine campagne contrairement aux flottes. Si une flotte est prise par la glace, elle empeche la circulation dans cette mer et ne peut pas bouger lors de cette campagne. " + "\n"
    return retour
def SoutienPopulaire():           
    region_cible = regions_terrestre[randint(0, len(regions_terrestre)-1)]
    retour = " Soutien Populaire : L'armée de **" + str(region_cible) + "** profite du soutien populaire, qui lui procure 0.5 de bonus en attaque lors de cette campagne. " + "\n"       
    return retour
def Blitzkrieg():
    region_cible = regions_terrestre[randint(0, len(regions_terrestre)-1)]
    retour = "Blitzkrieg : un reservoir de super carburant est decouvert en **" + str(region_cible) + "**. L'unité presente sur cette case peut se deplacer 2 fois pour la prochaine campagne. " + "\n"                       
    return retour   
def enlisement():
    region_cible = regions_terrestre[randint(0, len(regions_terrestre)-1)]
    retour = "Enlisement : L'unité terreste de **" + str(region_cible) + "** n'a pas été assez prudente et s'est enlisée dans un marais. Elle ne pourra bouger lors de la campagne suivante que si une unité alliée se trouve sur une case adjacente. " + "\n"
    return retour
def Miracle():
    region_cible = regions_ter_vides[randint(0, len(regions_ter_vides)-1)]
    retour = "Miracle : La magnifique region de **" + str(region_cible) + "** a construit une nouvelle merveille mondiale ! Elle gagne donc un nouvel arsenal representatif de son rayonnement culturel" + "\n"
    return retour
def Propagande():
    region_cible = pickNoArsenal()
    lucky_charms = pays[randint(0, len(pays)-1)]
    retour = "Aux armes ! : La population de **" + str(region_cible) + "** a succombé a la propagande de " + str(lucky_charms) + " ! Elle s'est spontanément organisée pour former une armée de ce dernier !" + "\n"
    return retour
def date():
    année = int(an + n_campagne/2)
    if n_campagne - 2*int(n_campagne/2) == 0:
        campagne = campagnes[0]
    else:
        campagne = campagnes[1]
    retour = str(campagne) + str(année) + ": " + "\n"
    print(retour)
    return retour
def LaTotale():
    global n_campagne
    retour, liste_actions = '', []
    for i in range(randint(2, 5)):
        dico_actions_possibles = {"1" : Pb(), "2" : Miracle(), "3" : Propagande(), "4" : MerGelée(), "5" : SoutienPopulaire(), "6" : None, "7": enlisement(), "8": isolement(), "9" : Rebellion(),"10":Blitzkrieg()}
        liste_actions.append(dico_actions_possibles[str(randint(1,6))])
    for i  in liste_actions:
        if i != None:
            retour = retour + " --> " + str(i)
    
    n_campagne += 1
    newdate(n_campagne)
     

    if retour =='':
        retour = "rien a signaler pour cette campagne."
    return retour
async def get_msg(channel: discord.TextChannel):
    return [message async for message in channel.history(limit=None)]
@client.event
async def on_ready():
    print(f"Connecté en tant que {client.user}")
    log_error("connected")    

@client.event
async def on_message(message: discord.Message):
    print(message.content)
    
    if message.content == "events" and message.author.id in admin_liste:
            print(message.channel)
            msg = str(date())+ "("+ str(n_campagne)+")" + str(LaTotale()+ "\n .")
            await message.channel.send(msg)
            await message.delete()
            
    elif message.content == "eventss":
        await message.channel.send("La fin du monde a commmencée... Inutile de continuer la partie.  😡")
        await message.delete()
    
    elif message.content.startswith("clean ") and message.author.id in admin_liste:
        try:
            n = int(message.content.split("clean ")[-1]) +1
        except:
            await message.reply("Entrez un entier")
            return
        messages = await get_msg(message.channel)
        for x in range(n):
            await messages[x].delete()
            
    elif message.content == "date" and message.author.id in admin_liste:
        await message.channel.send(date())
        await message.delete()
    
    elif message.content == "events_late" and message.author.id in admin_liste:
        msg = str(date() + "rien a signaler pour cette campagne."+ "\n .")
        await message.channel.send(msg)
        await message.delete()
    
    elif message.content.startswith("change date ") and message.author.id in admin_liste:
        try:       
            n_campagne = int(message.content.split("change date ")[-1])
            newdate(n_campagne)

        except:
            await message.reply("Entrez un entier")
            return
    elif message.content == "intro" and message.author.id in admin_liste:
        await message.channel.send(intro())
        await message.delete()
    elif message.content == "nostalgie!" and message.author.id in admin_liste:
        Nostalgie()
        
    elif message.content == "regret!" and message.author.id in admin_liste:
        regret()
        messages = await get_msg(message.channel)
        for x in range(2):
            await messages[x].delete()          
keep_alive()
client.run(TOKEN)
print("Démarrage du bot")
log_error("Démarrage du bot")
