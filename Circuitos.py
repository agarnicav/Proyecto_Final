from colorama import init, Fore, Back, Style

# Diagrama de un circuito RC. Utiliza caracteres ASCII para representar los componentes del circuito, como resistencias (R1) y un capacitor (C1). 

RC = '''
      ______________'''+Fore.RED+'''/\  /\  /\  /\ '''+Fore.RESET+'''______________
     |                '''+Fore.RED+'''\/  \/  \/'''+Fore.RESET+'''                 |
     |                    '''+Fore.RED+'''R1'''+Fore.RESET+'''                     |
     |                                           |
     |                                           |
     |                                           |
  '''+Fore.YELLOW+'''_______                                      '''+Fore.GREEN+'''_____
    '''+Fore.YELLOW+'''___    V1                                  '''+Fore.GREEN+'''_____ C1'''+Fore.RESET+'''
     |                                           |
     |                                           |
     |                                           |
     |                                           |
     |___________________________________________|

'''
# Diagrama de un circuito RL. Utiliza caracteres ASCII para representar los componentes del circuito, como resistencias (R1) y un inductor (bobina)(L1).
RL = '''
      ______________'''+Fore.RED+'''/\  /\  /\  /\ '''+Fore.RESET+'''______________
     |                '''+Fore.RED+'''\/  \/  \/'''+Fore.RESET+'''                 |
     |                    '''+Fore.RED+'''R1'''+Fore.RESET+'''                     |
     |                                           |
     |                                           |
     |                                           '''+Fore.BLUE+'''_)
  '''+Fore.YELLOW+'''_______                                        '''+Fore.BLUE+'''_)                 
    '''+Fore.YELLOW+'''___    V1                                    '''+Fore.BLUE+'''_) L1'''+Fore.RESET+'''                
     |                                           '''+Fore.BLUE+'''_)'''+Fore.RESET+'''
     |                                           |
     |                                           |
     |                                           |
     |___________________________________________|

'''
# Diagrama de un circuito RLC. Utiliza caracteres ASCII para representar los componentes del circuito, como resistencias (R1), un inductor (bobina) (L1) y un capacitor (C1).

RLC = '''
      ______________'''+Fore.RED+'''/\  /\  /\  /\ '''+Fore.RESET+'''______________
     |                '''+Fore.RED+'''\/  \/  \/'''+Fore.RESET+'''                 |
     |                    '''+Fore.RED+'''R1'''+Fore.RESET+'''                     |
     |                                           |
     |                                           |
     |                                           '''+Fore.BLUE+'''_)
  '''+Fore.YELLOW+'''_______                                        '''+Fore.BLUE+'''_)                 
    '''+Fore.YELLOW+'''___    V1                                    '''+Fore.BLUE+'''_) L1'''+Fore.RESET+'''                
     |                                           '''+Fore.BLUE+'''_)'''+Fore.RESET+'''
     |                                           |
     |                                           |
     |                     '''+Fore.GREEN+'''C1'''+Fore.RESET+'''                    |
     |____________________'''+Fore.GREEN+'''| |'''+Fore.RESET+'''____________________|
                          '''+Fore.GREEN+'''| |'''+Fore.RESET+'''
'''