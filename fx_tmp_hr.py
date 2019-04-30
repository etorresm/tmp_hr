import math
#/media/edwin/6F71AD994355D30E/Edwin/estacion_gr/tmp_hr # Ubicación
def dp():
    # Función que a partir de la temperatura, humedad y presión calcula otros parámetros
    t = float(input('Valor de la temperatura °C: '))
    rh = float(input('Valor de la humedad %: '))
    try:# Esto lo uso para poder poner un valor de default
        pres = float(input('Press  # hPascales bgt = 752.01:'))
    except:
        pres = 752.01
    td =243.04*(math.log(rh/100)+((17.625*t)/(243.04+t)))/(17.625-math.log(rh/100)-((17.625*t)/(243.04+t)))
    td2 = t - ((100-rh)/5.)
    rh = t*math.atan(0.151977*(rh + 8.313659)**(1/2)) + math.atan(t + rh) - math.atan(rh - 1.676331
            ) + 0.00391838*(rh)**(3/2) * math.atan(0.023101 * rh) - 4.686035
    e = (10**((7.5*td)/(237.3+td)))*6.11# Presión de vapor daturado
    e_s = 6.11*(10**((7.5*t)/(237.3+t)))# Presión de vapor total #https://ncalculators.com/meteorology/vapor-pressure-calculator.htm

    w = 621.97 * ((e)/(pres - e))# Tasa de mezcla
    w_s = 621.97 * ((e_s)/(pres - e_s))

    rh_2= (e*100)/e_s
    rh_3= (w*100)/w_s
    ## Sensación termica
    s_T = -8.78469476 + 1.61139411 * t + 2.338548839*rh - 0.14611605*t*rh - 0.012308094*(t**2) - 0.016424828*(rh**2) + 0.0022111732*(t**2)*rh + 0.00072546*t*(rh**2) - 0.000003582*(t**2)*(rh**2)
    print('__________________________')
    print('Presión hPa')
    print('Pres vapor agu a X tmp')
    print('Actual pres vap hPa:', e)
    print('Pres vap saturado hPa:', e_s)
    print('Humedad relativa:', rh_2)
    print('__________________________')
    print('Relación de mezcla g/kg')
    print('Masa vap agu / mas resto parcela')
    print('Tasa de mezcla:', w)
    print('Saturated mixing ratio: ', w_s)
    print('Humedad relativa:', rh_3)
    print('__________________________')
    print('sensación ter °C:', s_T)
    print('dewpoint 1 °C:', td)
    print('dewpoint 2 °C:', td2)
    print('wet bulb °C:', rh)
dp()
