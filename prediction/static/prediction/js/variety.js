function getYear(y)
{
  var y = document.getElementById(y);
  y.innerHTML = "";
  var year = new Date().getFullYear();
  var op = document.createElement("option");
  op.value = year;
  op.innerHTML = year;
  y.options.add(op);


}
function getMonth(m)
{
 var m = document.getElementById(m);
//m.innerHTML = null;
 var Month = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December'

}
var mon = new Date().getMonth();
for(i = mon+1 ; i<=12 ; i++)
{
var op = document.createElement("option");

   op.value = i;
   op.innerHTML = Month[i];
   m.options.add(op);
}

}
function getVariety(s,v)
         {
        var varietyInState = {0: [57, 73, 83, 65, 56, 63, 70, 29, 15, 68, 34],
                  1: [56, 75, 34, 50, 53, 20, 27, 18, 76, 59, 38,
                      9, 54, 57, 29, 15, 65,55, 45, 19, 44, 69, 63,
                      24, 79, 68, 70, 42, 35, 71, 46, 80, 86, 30,48,
                      90, 22, 21, 51, 73,  5, 25, 89, 16,  2, 14, 3,
                      1, 52, 81, 23,6, 11, 17, 13, 58, 31, 32, 67, 33],
                   2: [81, 57, 29, 39, 56, 15, 22, 86, 75, 45, 55, 24,
                       42, 68, 63, 69, 60,91, 34, 58, 80, 36,  1, 78, 12,
                       9, 84, 82, 53, 73, 10],
                  3: [65, 75, 57, 50, 39, 86, 56,  9, 78, 61, 67, 42, 28,
                      36, 83, 81, 69,63, 77, 60, 70],
                  4: [46, 72, 74, 57, 58, 66, 29,  8, 14, 67, 51, 31, 25,
                     36, 43, 47, 52,44,  0, 42, 90,  9, 55, 18],
                  5: [64, 57, 78, 84, 81, 18, 73, 56, 49, 59, 76,  7,  4,
                     65, 48, 70, 42,88, 34, 61, 69, 23, 28, 85, 12, 53, 27,
                     50, 62, 16,  5, 11, 58],
                  6: [56, 65, 54, 63, 71, 53, 42, 50, 89, 16, 41, 81, 75, 23, 59,  5, 69,
                     83, 86, 22, 20, 76, 32, 57, 48, 37, 33, 79, 51, 27, 82, 19, 38, 25,
                     35, 11, 73, 10, 45, 55, 21,  9, 46, 24, 40, 78],
                  7: [57, 81, 84, 70, 65, 56, 26,  9, 46, 87, 18],
                  8: [65, 67, 57, 39, 55, 44, 86, 71, 50, 60,45],
                  9: [70, 65,  9, 57, 81, 24, 84, 42],
                  10: [70, 57, 65, 87, 63, 71,  9, 66, 24, 82, 23, 64, 81]}
 rankVariety = {0: 'J3H',
 1: 'Jayadhar(Unginned)',
 2: 'Jarilla  (Ginned)',
 3: 'Jayadhar (Ginned)',
 4: 'V-797 22mm FIne',
 5: 'CJ 73 22mm FIne',
 6: 'A.K. 235  (Ginned)',
 7: 'Assam Comilla',
 8: 'Jayadhar 23mm-FIne',
 9: 'Kapas (Adoni)',
 10: 'Laxmi (Unginned)',
 11: 'DIGVIJAY 24mm, Superfine',
 12: 'Suvin 40mm(F)',
 13: 'F-846',
 14: 'Jayadhar',
 15: 'MCU-5 (A) 31mm FIne',
 16: 'HB6',
 17: 'F-505',
 18: 'H.B  (Ginned)',
 19: 'Mungari (Unginned)',
 20: 'H 420',
 21: 'Farm  (Ginned)',
 22: 'lra (Unginned)',
 23: '320F',
 24: 'Bengal Deshi (A) FIne',
 25: 'Laxmi',
 26: 'R.G.J-34 24mm-Fine',
 27: 'Farm (Unginned)',
 28: 'A.C. 122- H4',
 29: 'MCU 5',
 30: 'Farm PCG',
 31: 'Jaydhar',
 32: 'Savita',
 33: 'JKH 25',
 34: 'cotton (Ginned)',
 35: 'Mungari  (Ginned)',
 36: 'R-51  (Ginned)',
 37: 'R-51 (Unginned)',
 38: 'Hampi(Unginned)',
 39: 'LRA',
 40: 'LD-491',
 41: 'Hy-4  (Ginned)',
 42: 'Cotton (Ginned)',
 43: 'Hampi  (Ginned)',
 44: 'N-44',
 45: 'MCU',
 46: 'LD-327',
 47: 'Laxmi  (Ginned)',
 48: 'G-6',
 49: 'Shanker 4 31mm FIne',
 50: 'H4',
 51: 'F-1054',
 52: 'Krishna',
 53: 'CO-2 (Unginned)',
 54: 'CO2  (Ginned)',
 55: 'Varalaxmi',
 56: 'Cotton (Unginned)',
 57: 'Other',
 58: 'GCH',
 59: 'H.Y.4 (Unginned)',
 60: 'LRA  (Ginned)',
 61: 'Y-1',
 62: 'L-K',
 63: '170-CO2 (Unginned)',
 64: 'Shanker 6 (B) 30mm FIne',
 65: 'Desi',
 66: 'LH-1556',
 67: 'H-4(A) 27mm FIne',
 68: 'MCU-7',
 69: '170-C2  (Ginned)',
 70: 'American',
 71: 'A.K. 235 (Unginned)',
 72: 'Suyodhar  (Ginned)',
 73: 'Bunny',
 74: 'Varalakshmi  (Ginned)',
 75: 'DCH-32  (Ginned)',
 76: 'H.B (Unginned)',
 77: 'Cotton US',
 78: 'Local',
 79: 'L 147',
 80: 'PCO2',
 81: 'RCH-2',
 82: 'A-51-9 24mm. FIne',
 83: 'MECH-1',
 84: 'Narma BT Cotton',
 85: 'Mahico',
 86: 'DCH-32(Unginned)',
 87: 'J-34',
 88: 'H-6',
 89: 'Bramha',
 90: 'Aka-1 (Unginned)',
 91: 'Surabi'}

          var s = document.getElementById(s);
          var v = document.getElementById(v);
          v.innerHTML = "";
          var list = varietyInState[s.value]
          for(var l in list)
          {
            var op = document.createElement("option");
            op.value = list[l];
            op.innerHTML  = rankVariety[list[l]];
            v.options.add(op);
          }




         }
