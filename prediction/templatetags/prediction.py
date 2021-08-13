from django import template
register = template.Library()

VarietyRank ={
    'J3H': 0,
    'Jayadhar(Unginned)': 1,

    'Jarilla  (Ginned)': 2,
    'Jayadhar (Ginned)': 3,
    'V-797 22mm FIne': 4,
    'CJ 73 22mm FIne': 5,
    'A.K. 235  (Ginned)': 6,
    'Assam Comilla': 7,
    'Jayadhar 23mm-FIne': 8,
    'Kapas (Adoni)': 9,
    'Laxmi (Unginned)': 10,
    'DIGVIJAY 24mm, Superfine': 11,
    'Suvin 40mm(F)': 12,
    'F-846': 13,
    'Jayadhar': 14,
    'MCU-5 (A) 31mm FIne': 15,
    'HB6': 16,
    'F-505': 17,
    'H.B  (Ginned)': 18,
    'Mungari (Unginned)': 19,
    'H 420': 20,
    'Farm  (Ginned)': 21,
    'lra (Unginned)': 22,
    '320F': 23,
    'Bengal Deshi (A) FIne': 24,
    'Laxmi': 25,
    'R.G.J-34 24mm-Fine': 26,
    'Farm (Unginned)': 27,
    'A.C. 122- H4': 28,
    'MCU 5': 29,
    'Farm PCG': 30,
    'Jaydhar': 31,
    'Savita': 32,
    'JKH 25': 33,
    'cotton (Ginned)': 34,
    'Mungari  (Ginned)': 35,
    'R-51  (Ginned)': 36,
    'R-51 (Unginned)': 37,
    'Hampi(Unginned)': 38,
    'LRA': 39,
    'LD-491': 40,
    'Hy-4  (Ginned)': 41,
    'Cotton (Ginned)': 42,
    'Hampi  (Ginned)': 43,
    'N-44': 44,
    'MCU': 45,
    'LD-327': 46,
    'Laxmi  (Ginned)': 47,
    'G-6': 48,
    'Shanker 4 31mm FIne': 49,
    'H4': 50,
    'F-1054': 51,
    'Krishna': 52,
    'CO-2 (Unginned)': 53,
    'CO2  (Ginned)': 54,
    'Varalaxmi': 55,
    'Cotton (Unginned)': 56,
    'Other': 57,
    'GCH': 58,
    'H.Y.4 (Unginned)': 59,
    'LRA  (Ginned)': 60,
    'Y-1': 61,
    'L-K': 62,
    '170-CO2 (Unginned)': 63,
    'Shanker 6 (B) 30mm FIne': 64,
    'Desi': 65,
    'LH-1556': 66,
    'H-4(A) 27mm FIne': 67,
    'MCU-7': 68,
    '170-C2  (Ginned)': 69,
    'American': 70,
    'A.K. 235 (Unginned)': 71,
    'Suyodhar  (Ginned)': 72,
    'Bunny': 73,
    'Varalakshmi  (Ginned)': 74,
    'DCH-32  (Ginned)': 75,
    'H.B (Unginned)': 76,
    'Cotton US': 77,
    'Local': 78,
    'L 147': 79,
    'PCO2': 80,
    'RCH-2': 81,
    'A-51-9 24mm. FIne': 82,
    'MECH-1': 83,
    'Narma BT Cotton': 84,
    'Mahico': 85,
    'DCH-32(Unginned)': 86,
    'J-34': 87,
    'H-6': 88,
    'Bramha': 89,
    'Aka-1 (Unginned)': 90,
    'Surabi': 91}
    



State1 = {'0':'Orissa' ,
           '1':'Andhra Pradesh',
           '2':'Tamil Nadu ',
           '3':'Madhya Pradesh' ,
           '4':'Karnataka',
           '5':'Gujarat',
           '6':'Telangana',
           '7':'Punjab',
           '8':'Maharashtra',
           '9':'Haryana',
           '10':'Rajasthan'
           
         }    



Month = {
           '1':'January',
           '2':'February',
           '3':'March' ,
           '4':'April',
           '5':'May',
           '6':'June',
           '7':'July',
           '8':'August',
           '9':'September',
           '10':'October',
           '11':'November',
           '12':'December'
           
        }  




#   State = State1.get(post.get('state'))
#         month_for_html = Month.get(post.get('month'))
#         variety =  get_key_of_variety((int(post.get('variety'))))
      
def showmonth(m):
    
    return Month.get(str(m))

register.filter('showmonth',showmonth)


def showstate(s):
    
    return State1.get(str(s))

register.filter('showstate',showstate)

def get_key_of_variety(variety):
    for key , value in  VarietyRank.items():
        if variety == value:
            return key
    
    
def showvariety(v):
    
    
    return get_key_of_variety(int(v))

register.filter('showvariety',showvariety)    


    


            


    
    


