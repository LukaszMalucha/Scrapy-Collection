# -*- coding: utf-8 -*-
"""
Created on Thu May  6 19:16:43 2021

@author: LukaszMalucha
"""

import pandas as pd
import numpy as np



dataset = pd.read_csv("1.csv", encoding="utf-8")

dataset = dataset.fillna("")

dataset["address_area_2"] = dataset["address_area_2"].str.replace(",", "").str.strip()


dataset["address_area_2"] = np.where(dataset["address_area_2"].str.len() < 1, dataset["address_area_1"],  dataset["address_area_2"] )


dataset["address_number"] = dataset["address_number"].str.replace("Apartment", "")
dataset["address_number"] = dataset["address_number"].str.strip()
dataset["address_number"] = dataset["address_number"].str.replace(",", "")






dataset["address_area_2"] = np.where(dataset["address_number"].str.len() > 6, dataset["address_number"],  dataset["address_area_2"] )
dataset["address_number"] = np.where(dataset["address_number"].str.len() > 6, "1",  dataset["address_number"] )



dataset["price"] = dataset["price"].str.replace("€", "").str.replace(",", "")


dataset = dataset.rename(columns={"address_area_1": "address", "address_area_2": "area", "address_number": "number"})


dataset = dataset[[ 'area', 'address', 'number',  'price','date', 'property_type']]

dataset["area"] = np.where(dataset["address"].str.contains("Coopers"), "Old Quarter",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Caislean"), "An Caislean",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("An Cais"), "An Caislean",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Aylsbury"), "Aylsbury",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains(" Lake"), "Classis Lake",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Classis"), "Classis Lake",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Coolroe"), "Coolroe",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Glincool"), "Glincool",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Greenfield"), "Greenfield",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Heathfield"), "Heathfield",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Inniscarra"), "Inniscarra",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Innishmore"), "Innishmore",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Maglin"), "Maglin",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Mukerry"), "Muskerry Estate",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Parknamore"), "Parknamore",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("The Crescent"), "The Crescent",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("The Maltings"), "The Maltings",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Westcourt"), "Westcourt",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains(" Quarter"), "Old Quarter",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains(" Quater"), "Old Quarter",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Clincool Gardens"), "Maglin",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Glincool"), "Maglin",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Glencool"), "Maglin",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("East Side"), "Carrigrohane",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Chapel Lane"), "Town Center",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Steeplewoods"), "Steeplewoods",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Whitethorn Avenue"), "Inniscarra View",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Carriglee"), "Carrigrohanebeg",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Willow Court"), "Carrigrohanebeg",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("West Village"), "West Village",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Link Road"), "Link Road",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Wyndham Downs"), "Wyndham Downs",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Leecourt"), "Leecourt",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Millers Court"), "Old Quarter",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Carrigdene"), "Town Center",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Daffodil Fields"), "Daffodil Fields",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Time Square"), "Town Center",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Manor Hill"), "Manor Hill",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Poulavone"), "Town Center",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Pulavone"), "Town Center",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Tara"), "An Caislean",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Oldcourt"), "Greenfield",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Cedardale"), "Carrigrohanebeg",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Churchview"), "Church View",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Tus Abhaile"), "Town Center",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Distillery Court"), "The Maltings",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Town Centre"), "Town Centre",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Glendower Court"), "Glendower Court",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Shalimar Court"), "Shalimar Court",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Chapel Lane Row"), "Town Center",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Main Road"), "Town Center",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Quadrants"), "The Quadrants",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Main Street"), "Town Center",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("East Gate"), "Town Center",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Father Sexton Place"), "Carrigrohane",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Fionn Laoi"), "Fionn Laoi",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Green Road"), "Maglin",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Town Centre"), "Town Center",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("The Cresent Old Fort Road"), "The Cresent",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Coopers Grange"), "Old Quarter",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("The Cresent"), "Old Quarter",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("The Willows"), "Carrigrohanebeg",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Church View"), "Town Center",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Cranford Pines"), "Beech Park",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Kerry Pike"), "Kerry Pike",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Leesdale Drive"), "Leesdale Drive",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Ovens"), "Ovens",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Highfield"), "Highfield",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Leeview"), "Lackenshoneen",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Aherla"), "Aherla",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Castlepark"), "Castlepark",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Model Farm Road"), "Model Farm Road",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Rosewood"), "Rosewood",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Caisleán"), "An Caislean",  dataset["area"] )
dataset["area"] = np.where(dataset["area"].str.contains("Classes"), "Classis Lake",  dataset["area"] )
dataset["area"] = np.where(dataset["area"].str.contains("Classis"), "Classis Lake",  dataset["area"] )
dataset["area"] = np.where(dataset["area"].str.contains("Clases"), "Classis Lake",  dataset["area"] )
dataset["area"] = np.where(dataset["area"].str.contains("East Side"), "Powdermills",  dataset["area"] )
dataset["area"] = np.where(dataset["area"].str.contains("Greenfields Road"), "Greenfield",  dataset["area"] )
dataset["area"] = np.where(dataset["area"].str.contains("Flynns Road West Village"), "West Village",  dataset["area"] )
dataset["area"] = np.where(dataset["area"].str.contains("The Old Quarter"), "Old Quarter",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("The Cloisters"), "The Cloisters",  dataset["area"] )
dataset["area"] = np.where(dataset["area"].str.contains("Coolroe"), "Coolroe",  dataset["area"] )
dataset["area"] = np.where(dataset["area"].str.contains("Quater"), "Old Quarter",  dataset["area"] )
dataset["area"] = np.where(dataset["area"].str.contains("An Caislean"), "An Caislean",  dataset["area"] )
dataset["area"] = np.where(dataset["area"].str.contains("Inniscarra View Estate"), "Inniscarra View",  dataset["area"] )
dataset["area"] = np.where(dataset["area"].str.contains("Main Road"), "Town Center",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Bellview"), "Westcourt",  dataset["area"] )
dataset["area"] = np.where(dataset["area"].str.contains("The Maltings"), "The Maltings",  dataset["area"] )
dataset["area"] = np.where(dataset["area"].str.contains("Heathfield"), "Heathfield",  dataset["area"] )
dataset["area"] = np.where(dataset["area"].str.contains("Poulavone"), "Town Center",  dataset["area"] )
dataset["area"] = np.where(dataset["area"].str.contains("0ld Quarter"), "Old Quarter",  dataset["area"] )
dataset["area"] = np.where(dataset["area"].str.contains("Leesdale Drive"), "Carrigrohane",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Muskerry Estate"), "Muskerry Estate",  dataset["area"] )
dataset["area"] = np.where(dataset["address"].str.contains("Castle Park"), "Castlepark",  dataset["area"] )

dataset["area"] = dataset["area"].str.strip()


dataset["geocode"] = ""



dataset["geocode"] = np.where(dataset["area"] == "Maglin", "51.88135112776452, -8.59523805920491",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Classis Lake", "51.88586099008718, -8.62822296864587",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Old Quarter", "51.89008441064981, -8.590014945710507",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "The Cloisters", "51.88453436126935, -8.578140286193113",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "West Village", "51.886701875920906, -8.606268807280973",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "The Maltings", "51.88503727921537, -8.591352822622822",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Coolroe", "51.885279789132504, -8.622716969745719",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "An Caislean", "51.88419579207018, -8.604721941977742",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Parknamore", "51.88458744794133, -8.609309161051812",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Castle Road", "51.88237120146108, -8.598641786193197",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Muskerry Estate", "51.885514844369936, -8.596310161258103",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Old Fort Road", "51.88988509759098, -8.59066895920469",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Highfield Park", "51.88438631124541, -8.574891410855766",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Westcourt", "51.88681255417706, -8.616295628522487",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Greenfield", "51.87768330900382, -8.61608163310892",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Castlepark", "51.88650616536384, -8.58533217454591",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Rosewood", "51.88865181082447, -8.575978970851866",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "The Willows", "51.89301140145297, -8.581593590126793",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Town Center", "51.8878563321983, -8.600737381727024",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Carriglee", "51.89320554364949, -8.582261828522315",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Carrigrohanebeg", "51.89309917070151, -8.580849757357647",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Limeworth", "51.88244387440602, -8.582059330369558",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "West Village", "51.88656943500571, -8.60609714591646",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "The Quadrants", "51.8890702782036, -8.589706799326772",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "The Stables", "51.88380436406558, -8.622683203381243",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Leo Murphy Terrace", "51.888591280385164, -8.583440501534145",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Aylsbury", "51.88284449037205, -8.620440916875388",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Wyndham Downs", "51.88595620016782, -8.620113757357807",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Carriganarra", "51.88456579585057, -8.579854607281877",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Hazel Grove", "51.88270220033945, -8.594207045710691",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Cranford Pines", "51.88391871868656, -8.585827588040098",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Beech Park", "51.884462825784524, -8.586660730369518",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Church View", "51.88549636879165, -8.592625889887055",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "The Crescent", "51.88974689003794, -8.592724974545812",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Wyndham Downs", "51.88594295587414, -8.620296147557605",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Tudor Grove", "51.88555121291465, -8.591538215028342",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Westgrove", "51.88676931020199, -8.6146432996872",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Carrigrohane", "51.89608063198051, -8.56348113795949",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Station Cross", "51.88366424957323, -8.588997728522568",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Innishmore", "51.88897474404985, -8.608958999892096",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Powdermills", "51.89225015549648, -8.586096438526356",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Willow Grove", "51.882509982430086, -8.612375401534269",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Castleknock", "51.88198791175574, -8.595112470852024",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Station Road", "51.885856656204545, -8.590996730369481",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Leeview", "51.885856656204545, -8.590996730369481",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Heathfield", "51.88275370396547, -8.57522707085204",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Greystones", "51.88708566318779, -8.572495537963082",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Leesdale Court", "51.89042385266594, -8.583049957357712",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Avoncourt", "51.88515208061713, -8.612719189887075",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Cois Na Cora", "51.89115617169389, -8.586177713181245",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "An Caisleann", "51.89115617169389, -8.586177713181245",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Cois Na Cora", "51.89115617169389, -8.586177713181245",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Fionn Laoi", "51.89295672639931, -8.577244778805012",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Coolroe Meadows", "51.88363432099277, -8.616138226350916",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Greenfields", "51.87941701969475, -8.620193493581136",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Steeplewoods", "51.88978058994379, -8.565944853663783",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Greenfield", "51.88072634468435, -8.611355403381312",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Highfield", "51.88483134751023, -8.573114016875365",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Inniscarra View", "51.88901621244116, -8.572065214668026",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Manor Hill", "51.89121035709487, -8.575907457357648",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Shalimar Court", "51.88896130535807, -8.578969730369383",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Shalimar Court", "51.88896130535807, -8.578969730369383",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "The Cloisters", "51.88453436126935, -8.578108099687265",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Leecourt", "51.8915162277775, -8.581342570851831",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Coolroe Heights", "51.8915162277775, -8.581342570851831",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Daffodil Fields", "51.89114262893351, -8.573402430369397",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Glendower Court", "51.890963893776494, -8.579131855510711",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Mukerry Estate", "51.88554133320571, -8.596438907281483",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Glendower Court", "51.89097713659068, -8.579260601534097",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Glendower Court", "51.89097713659068, -8.579260601534097",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Ovens", "51.88127654707539, -8.658682937965343",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Castle Road", "51.88234227885883, -8.59817565735788",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Carrigrohane", "51.89118108080445, -8.570433423222292",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "West Village", "51.88675485217772, -8.606397553304374",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "West Village", "51.88675485217772, -8.606397553304374",  dataset["geocode"] )
dataset["geocode"] = np.where(dataset["area"] == "Castlepark", "51.88653927567583, -8.585310716875346",  dataset["geocode"] )


dataset["area"] = dataset["area"].str.strip()

dataset = dataset[dataset["area"] != "Inniscarra"]
dataset = dataset[dataset["area"] != "Ballyburden"]
dataset = dataset[dataset["area"] != "Kilnaglory"]
dataset = dataset[dataset["area"] != "Killumney Road"]
dataset = dataset[dataset["area"] != "Blarney"]
dataset = dataset[dataset["area"] != "Lackenshoneen"]
dataset = dataset[dataset["address"] != "Doire Loin"]
dataset = dataset[dataset["area"] != "Lackenshoneen"]
dataset = dataset[dataset["area"] != "Kerry Pike"]
dataset = dataset[dataset["area"] != "Aherla"]
dataset = dataset[~dataset["address"].str.contains("Grange Hill")]
dataset = dataset[dataset["area"] != "Model Farm Road"]

dataset["full_address"] = dataset["number"] + " " + dataset["address"] + ", " + dataset["area"]

dataset = dataset[dataset["price"].str.len() == 6]








dataset.to_csv("ballincollig_sold.csv", index=False)









