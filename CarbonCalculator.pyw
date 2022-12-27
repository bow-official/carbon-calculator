from guizero import App, Text, TextBox, Box, PushButton
import requests
import webbrowser
import time
irapi = "https://cloud.mymetaverse.io/users/p2e/614fbb71f2da386d1906fe55"
response_ir = requests.get(irapi)
irpull = response_ir.json()
siapi = "https://cloud.mymetaverse.io/users/p2e/5f6025dc4c86f778d453dc98"
response_si = requests.get(siapi)
sipull = response_si.json()
imapi = "https://cloud.mymetaverse.io/users/p2e/638a5b606855963bec5f9e82"
response_im = requests.get(imapi)
impull = response_im.json()

def learning():
    learnurl = "https://mymetaverse.io/learn/carbon-sink-NFTs"
    webbrowser.open(learnurl)
    
def calc_infrealm():
    irpool = round((irpull['assignedAmount']))
    irtier_one_metaprofiles = str(irtier_one_metaprofiles_a.value)
    irtier_two_metaprofiles = str(irtier_two_metaprofiles_a.value)
    irtier_three_metaprofiles = str(irtier_three_metaprofiles_a.value)
    ir_tier_one = round(((irpool / 15  * (0.5)) * int(irtier_one_metaprofiles)))
    ir_tier_two = round(((irpool / 15  * (0.3)) * int(irtier_two_metaprofiles)))
    ir_tier_three = round(((irpool / 15  * (0.2)) * int(irtier_three_metaprofiles)))
    irtotal = str(ir_tier_one + ir_tier_two + ir_tier_three)
    irmoney = str(round(int(irtotal) / 5))
    irtotal_msg = Text(results, color="green", text=irtotal + " KG of Carbon from Infinity Realms ($" + irmoney + ")")
    
def calc_survinf():
    sipool = round((sipull['assignedAmount']))
    sitier_one_metaprofiles = str(sitier_one_metaprofiles_a.value)
    sitier_two_metaprofiles = str(sitier_two_metaprofiles_a.value)
    sitier_three_metaprofiles = str(sitier_three_metaprofiles_a.value)
    si_tier_one = round(((sipool / 15  * (0.5)) * int(sitier_one_metaprofiles)))
    si_tier_two = round(((sipool / 15  * (0.3)) * int(sitier_two_metaprofiles)))
    si_tier_three = round(((sipool / 15  * (0.2)) * int(sitier_three_metaprofiles)))
    sitotal = str(si_tier_one + si_tier_two + si_tier_three)
    simoney = str(round(int(sitotal) / 5))
    sitotal_msg = Text(results, color="green", text=sitotal + " KG of Carbon from Survival Infinity ($" + simoney + ")")
    
def calc_impulse():
    impool = round((impull['assignedAmount']))
    imtier_one_metaprofiles = str(imtier_one_metaprofiles_a.value)
    imtier_two_metaprofiles = str(imtier_two_metaprofiles_a.value)
    imtier_three_metaprofiles = str(imtier_three_metaprofiles_a.value)
    im_tier_one = round(((impool / 15  * (0.5)) * int(imtier_one_metaprofiles)))
    im_tier_two = round(((impool / 15  * (0.3)) * int(imtier_two_metaprofiles)))
    im_tier_three = round(((impool / 15  * (0.2)) * int(imtier_three_metaprofiles)))
    imtotal = str(im_tier_one + im_tier_two + im_tier_three)
    immoney = str(round(int(imtotal) / 5))
    imtotal_msg = Text(results, color="green", text=imtotal + " KG of Carbon from Impulse ($" + immoney + ")")
    
app = App("Carbon Calculator", height=1000, bg="white")
header = Text(app, text="Carbon Calculator v1 - Made by BowFun", size=16)
subtext = Text(app, text="Calculate your earning of Carbon without worrying about math!")
spacer = Text(app, text=" ", size=5)
learn = PushButton(app, text="Learn about Carbon!", command=learning, width=15, height=1)
results = Box(app)
infrealm = Box(app)
survinf = Box(app)
impulse = Box(app)

irspacer = Text(infrealm, text=" ", size=5)
irheader = Text(infrealm, text="Infinity Realms", size=14)
irsubtext = Text(infrealm, text="Calculate your earnings from Infinity Realms.")
irspacer_two = Text(infrealm, text=" ", size=10)
irtier_one_metaprofiles_explain = Text(infrealm, text="Enter the number of MetaProfiles you have in tier one:", size=10)
irtier_one_metaprofiles_a = TextBox(infrealm, text=0)
irtier_one_metaprofiles_explain = Text(infrealm, text="Enter the number of MetaProfiles you have in tier two:", size=10)
irtier_two_metaprofiles_a = TextBox(infrealm, text=0)
irtier_one_metaprofiles_explain = Text(infrealm, text="Enter the number of MetaProfiles you have in tier three:", size=10)
irtier_three_metaprofiles_a = TextBox(infrealm, text=0)
irspacer_three = Text(infrealm, text=" ", size=5)
calculate_button = PushButton(infrealm, command=calc_infrealm, text="Calculate Carbon")

sispacer = Text(survinf, text=" ")
siheader = Text(survinf, text="Survival Infinity", size=14)
sisubtext = Text(survinf, text="Calculate your earnings from Survival Infinity.")
sispacer_two = Text(survinf, text=" ", size=10)
sitier_one_metaprofiles_explain = Text(survinf, text="Enter the number of MetaProfiles you have in tier one:", size=10)
sitier_one_metaprofiles_a = TextBox(survinf, text=0)
sitier_one_metaprofiles_explain = Text(survinf, text="Enter the number of MetaProfiles you have in tier two:", size=10)
sitier_two_metaprofiles_a = TextBox(survinf, text=0)
sitier_one_metaprofiles_explain = Text(survinf, text="Enter the number of MetaProfiles you have in tier three:", size=10)
sitier_three_metaprofiles_a = TextBox(survinf, text=0)
sispacer_three = Text(survinf, text=" ", size=5)
calculate_button = PushButton(survinf, command=calc_survinf, text="Calculate Carbon")

imspacer = Text(impulse, text=" ")
imheader = Text(impulse, text="Impulse", size=14)
imsubtext = Text(impulse, text="Calculate your earnings from Impulse.")
imspacer_two = Text(impulse, text=" ", size=10)
imtier_one_metaprofiles_explain = Text(impulse, text="Enter the number of MetaProfiles you have in tier one:", size=10)
imtier_one_metaprofiles_a = TextBox(impulse, text=0)
imtier_one_metaprofiles_explain = Text(impulse, text="Enter the number of MetaProfiles you have in tier two:", size=10)
imtier_two_metaprofiles_a = TextBox(impulse, text=0)
imtier_one_metaprofiles_explain = Text(impulse, text="Enter the number of MetaProfiles you have in tier three:", size=10)
imtier_three_metaprofiles_a = TextBox(impulse, text=0)
imspacer_three = Text(impulse, text=" ", size=5)
calculate_button = PushButton(impulse, command=calc_impulse, text="Calculate Carbon")

app.display()
