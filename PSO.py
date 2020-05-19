import numpy as np # linear algebra
from scipy.stats import wilcoxon
import random


#Sigmoid Fonksiyonu - OneMax Probleminde kullanılır.
def sigmoidFunc(x):
  return 1 / (1 +np.exp(-x))
# --------------------------------------------------
# Algoritmanın Objective Function: Cost Function - Maliyet
def OneMax(particle_Value):
    maliyet=0
    for i in particle_Value:
        if sigmoidFunc(i)>=0.5:
            maliyet=maliyet+1
    return maliyet

#Hız formülünün hesaplanması için değerler
w=0.005#w = 0.005 
c1=0.005#c1 = 0.005 #self confidence değeri - particle (parçacık)
c2=0.009#c2 = 0.009 #swarm confidence değeri - swarm (sürü)
parcacik_Sayisi = 40 #parçacık sayısı - POPULATION
D=100  #D=100,500,10000
#Toplam NFE Sayısı
toplam_İterasyon = 100000
boyutHatasi = 0.1

#Random değerlerle vektör oluşturma
particle_Value = np.array([np.array([(-1) ** (bool(random.getrandbits(1))) * random.random()
for _ in range(D)])
    for _ in range(parcacik_Sayisi)])
pbest_position=particle_Value.copy()
pbest_fitness_value = np.zeros(parcacik_Sayisi)
gbest_position=np.zeros(D)
gbest_baslangic = 0.0
for i in range(parcacik_Sayisi):
    aday_fitness = OneMax(particle_Value[i]) #parçacıkların uygunluk değerleri hesaplanıyor
    pbest_fitness_value[i] = aday_fitness #uygunluk fonksiyonuna göre pozisyonlar güncellenecek
    if(gbest_baslangic < aday_fitness):
        gbest_baslangic = aday_fitness
        gbest_position=particle_Value[i]
velocity_vector= np.array([random.random()  #hız konum vektörü
        for _ in range(D)])

iteration = 0
while iteration < toplam_İterasyon:
    iteration = iteration + 1
    for i in range(parcacik_Sayisi):
        aday_fitness = OneMax(particle_Value[i])
        if(pbest_fitness_value[i] < aday_fitness):
            pbest_fitness_value[i] = aday_fitness
        if(gbest_baslangic < aday_fitness):
            gbest_baslangic = aday_fitness
            gbest_position=particle_Value[i]
    print("Bulunan En İyi Konumun Uygunluk Değeri: ",gbest_baslangic,"yineleme numarasına kadar ", iteration)
    if(D-gbest_baslangic < boyutHatasi):
            break
    for i in range(parcacik_Sayisi):
        firstVelocity=velocity_vector[i]  #yeni hız hesabı
        new_velocity= (w*firstVelocity) + (c1*random.random()) * (pbest_position[i] - particle_Value[i]) + (c2*random.random()) * (gbest_position-particle_Value[i])
        new_position = new_velocity + particle_Value[i]
        for d in new_position:
            d = np.maximum(d, -1);
            d = np.minimum(d, 1);
        a=new_velocity
        particle_Value[i] = new_position.copy()
        
       
print("Bulunan En İyi Konum (best_Position) ",gbest_position, "iterasyon sayısı ", iteration)
#PSO_array =np.array([])
#for i in range(0,30):
#            best_globalBest = np.min(gbest_position)
#            PSO_array=np.append(PSO_array,best_globalBest)

#wilcoxon Hesabı
#med_gbest = np.median(gbest_position)
#mean_gbest = np.mean(gbest_position)

#worst_gbest = np.max(gbest_position)
#std_gbest= np.std(gbest_position)
#wilcoxonValue = wilcoxon(gbest_position)
#print(wilcoxonValue)

#------------------------ D=100, best_gbest değerleri arrayde tutma 30 Run
#PSO_array =np.array( [0.013948137718705844,0.013948137718705844,0.06696503754861632,0.0714767613231091,0.056101755340186577,0.018172356076727958,0.006620318140643455,0.06739719608516784,0.4358890553206116,
#            0.07175993057203933,0.006890083018406434,0.4405023200617695,0.013161011680815404, 0.02028838551997103,0.18805389033428466,0.001496700649763677,0.2697742840796684,0.04322261103398334,0.15823941813770404,
#            0.060130198890374964,0.03761129854138817,0.10559857743135925,0.043513670804408155,0.17126867878451013,0.04271187254798958,0.053189958907321144,0.07375779759272805,0.11889313325006878,0.20934386592060256,0.20720827740629355])

#------------------------ D=500, best_gbest değerleri arrayde tutma 30 Run
#PSO_array =np.array( [0.11754793079697795,0.031601674227415444,0.07215956233957638,0.5125380033802425,0.012903756911129383,0.035423950773346646,0.1437740364755065,0.26308949543749416,0.09917853678660615,0.18295903968168054,0.2538663879899694,0.19330532295820668,0.01044926134070201,0.02964519794657966,
#                      0.19379768394155805,0.14313768021320644,0.07484129842243714,0.02998074445106902,0.14355154949977855,0.02198008933851009,0.005725796727632307,0.007424611079770382,0.0010117064651082308,0.09197013784312547,0.25309616133490653,0.004875549710011473,0.2630442864188927,0.06611200450070642,0.014792964851308543,0.05331747303772566])
#PSO_array =np.array([0.22824028998909054,0.035540647271130044,0.03629272761152125,0.3845285497548532,0.004741097561973939,0.07070672989044172,0.2924840594111654,0.28180691306491523,0.1602755097184767,0.0036061806582794453,0.2849369232923976,0.04801989937557724,0.14434120828888553,
#                    0.7015965709030323,0.02666487754662966,0.04938348290306971, 0.24909550749588916,0.04034545211302176,0.014620576416888492,0.13173129758186974,
#                    0.011753528755119591,0.03362757347917478,0.20297901960940026,0.020167143117145292,0.030139733360318333,0.006405988181568678,0.007342884424722529,0.0005810872467598704,0.11528862380611671,0.21080489009401915])
#med_gbest = np.median(PSO_array)
#print('Median:',med_gbest)
#mean_gbest = np.mean(PSO_array)
#print('Mean:',mean_gbest)
#best_PSOArray = np.min(PSO_array)
#print('Best Value:',best_PSOArray)
#worst_PSOArray = np.max(PSO_array)
#print('Worst Value:',worst_PSOArray)
#std_PSOArray= np.std(PSO_array)
#print('Standard Deviation Value:',std_PSOArray)
#wilcoxonValue = wilcoxon(PSO_array)
#print('Wilcoxon Value:',wilcoxonValue)
#
#PSO_array =np.array([0.0011651808027088417,0.0026895353742415603,0.002164710774169054,0.0023251480190139367,0.005277110056408907,0.0038407398242391107,0.005124856299829081,0.0012908510140530348,0.0021909056051584736,
#                     0.007028359876563611,0.000974003899462516,0.0014331983095163085,0.000502933810845727,0.006108309747370961,0.002125787521954476,0.008994153476226206,0.0025730986375139915,0.0028930234179803064,0.00585707795208367,0.00023797210224091314,
#                     0.003442833487735697,0.006193429402063887,0.0025029423020504478,0.0008388632198655013,0.00306139268797469,0.0019991923929994944,0.003888966456436887,0.00421074198409148,0.002258184231048712,0.0014621885662545464])
#med_gbest = np.median(PSO_array)
#print('Median:',med_gbest)
#mean_gbest = np.mean(PSO_array)
#print('Mean:',mean_gbest)
#best_PSOArray = np.min(PSO_array)
#print('Best Value:',best_PSOArray)
#worst_PSOArray = np.max(PSO_array)
#print('Worst Value:',worst_PSOArray)
#std_PSOArray= np.std(PSO_array)
#print('Standard Deviation Value:',std_PSOArray)
#wilcoxonValue = wilcoxon(PSO_array)
#print('Wilcoxon Value:',wilcoxonValue)
#PSO_array =np.array([0.0014124344198992358,0.002215271770698628,0.0026130414795900725,0.003270153824631206,0.00040266653189788846,0.000514022700491851,0.002851137995421562,0.0017581883519716464,0.0011893530439408585,
#                     0.0011240309780352954,0.0014429113881687834,0.005810927982182926,0.0031221646550099787,0.003319386386586768,0.004976938553068662,0.00652299647385428,0.0013830085944449206,0.002333497124298348,0.0005296224608811887,0.0009963634856617306,
#                     0.002336123252667528,0.0001588232061854383,0.001803125742828651,0.0035985109398718788,0.006366183742790979,0.0001636206185775934,0.003049603142894193,0.0018164096571179167,0.003275057986386762,0.0030162848197482174])
med_gbest = np.median(PSO_array)
print('Median:',med_gbest)
mean_gbest = np.mean(PSO_array)
print('Mean:',mean_gbest)
best_PSOArray = np.min(PSO_array)
print('Best Value:',best_PSOArray)
worst_PSOArray = np.max(PSO_array)
print('Worst Value:',worst_PSOArray)
std_PSOArray= np.std(PSO_array)
print('Standard Deviation Value:',std_PSOArray)
wilcoxonValue = wilcoxon(PSO_array)
print('Wilcoxon Value:',wilcoxonValue)


    
    