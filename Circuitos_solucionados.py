from colorama import init, Fore, Back, Style

def circuitoRC(V:float,VR:float,VC:float,I:float,R:float,C:float):
    print('''
                      '''+Fore.RED+f'''R1 = {R} Ω'''+Fore.RESET+'''         
      ______________'''+Fore.RED+'''/\  /\  /\  /\ '''+Fore.RESET+'''_______________
     |                '''+Fore.RED+'''\/  \/  \/'''+Fore.RESET+'''                  |
     |                   '''+Fore.RED+'''VR(t)'''+Fore.RESET+'''                    |
     |                                            |
     |               '''+Fore.MAGENTA+'''_______________'''+Fore.RESET+'''              |
     |              '''+Fore.MAGENTA+'''|               |'''+Fore.RESET+'''             |
  '''+Fore.YELLOW+'''_______           '''+Fore.MAGENTA+'''|               |'''+Fore.GREEN+'''           _____
  '''+Fore.YELLOW+'''  ___    V(t)     '''+Fore.MAGENTA+'''|      I(t)     |'''+Fore.GREEN+f'''     VC(t) _____ C1 = {C} µF'''+Fore.RESET+'''
     |              '''+Fore.MAGENTA+'''|               V'''+Fore.RESET+'''             |
     |              '''+Fore.MAGENTA+'''|'''+Fore.RESET+'''                             |
     |                                            |
     |                                            |
     |____________________________________________|
    
    '''+Fore.YELLOW+f'''{V}
    '''+Fore.RED+f'''{VR}
    '''+Fore.GREEN+f'''{VC}
    '''+Fore.MAGENTA+f'''{I}'''+Fore.RESET+'''
''')
    
def circuitoRL(V:float,VR:float,VL:float,I:float,R:float,L:float):
    print(f'''
                      '''+Fore.RED+f'''R1 = {R} Ω'''+Fore.RESET+'''        
      ______________'''+Fore.RED+'''/\  /\  /\  /\ '''+Fore.RESET+'''_______________
     |                '''+Fore.RED+'''\/  \/  \/'''+Fore.RESET+'''                  |
     |                   '''+Fore.RED+'''VR(t)'''+Fore.RESET+'''                    |
     |                                            |
     |               '''+Fore.MAGENTA+'''_______________'''+Fore.RESET+'''              |
     |              '''+Fore.MAGENTA+'''|               |'''+Fore.BLUE+'''             _)
  '''+Fore.YELLOW+'''_______           '''+Fore.MAGENTA+'''|               |'''+Fore.BLUE+'''             _)
  '''+Fore.YELLOW+'''  ___    V(t)     '''+Fore.MAGENTA+'''|      I(t)     |'''+Fore.BLUE+f'''     VL(t)   _)  L1 = {L} H'''+Fore.RESET+'''
     |              '''+Fore.MAGENTA+'''|               V'''+Fore.BLUE+'''             _)'''+Fore.RESET+'''
     |              '''+Fore.MAGENTA+'''|'''+Fore.RESET+f'''                             |
     |                                            |
     |                                            |
     |____________________________________________|
    
    '''+Fore.YELLOW+f'''{V}
    '''+Fore.RED+f'''{VR}
    '''+Fore.BLUE+f'''{VL}
    '''+Fore.MAGENTA+f'''{I}'''+Fore.RESET+'''
''')

def circuitoRLC(V:float,VR:float,VL:float,VC:float,I:float,R:float,L:float,C:float):
    print(f'''
                      '''+Fore.RED+f'''R1 = {R} Ω'''+Fore.RESET+'''        
      ______________'''+Fore.RED+'''/\  /\  /\  /\ '''+Fore.RESET+'''_______________
     |                '''+Fore.RED+'''\/  \/  \/'''+Fore.RESET+'''                  |
     |                   '''+Fore.RED+'''VR(t)'''+Fore.RESET+'''                    |
     |                                            |
     |               '''+Fore.MAGENTA+'''_______________'''+Fore.RESET+'''              |
     |              '''+Fore.MAGENTA+'''|               |'''+Fore.BLUE+'''             _)
  '''+Fore.YELLOW+'''_______           '''+Fore.MAGENTA+'''|               |'''+Fore.BLUE+'''             _)
  '''+Fore.YELLOW+'''  ___    V(t)     '''+Fore.MAGENTA+'''|      I(t)     |'''+Fore.BLUE+f'''     VL(t)   _)  L1 = {L} H'''+Fore.RESET+'''
     |              '''+Fore.MAGENTA+'''|               V'''+Fore.BLUE+'''             _)'''+Fore.RESET+'''
     |              '''+Fore.MAGENTA+'''|'''+Fore.RESET+f'''                             |
     |                                            |
     |                                            |
     |                   '''+Fore.GREEN+'''VC(t)'''+Fore.RESET+'''                    |
     |____________________'''+Fore.GREEN+'''| |'''+Fore.RESET+'''_____________________|    
                          '''+Fore.GREEN+'''| |'''+Fore.RESET+'''  
                        '''+Fore.GREEN+f'''C1 = {C} µF 

    '''+Fore.YELLOW+f'''{V}
    '''+Fore.RED+f'''{VR}
    '''+Fore.BLUE+f'''{VL}
    '''+Fore.GREEN+f'''{VC}
    '''+Fore.MAGENTA+f'''{I}'''+Fore.RESET+'''
''')