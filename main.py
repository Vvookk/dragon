import sys, time

def typing(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)

def start():
    typing("Hej, bawimy się w pajtonowanko, co?")
    time.sleep(2)
    typing("\nSuper! :)")
    time.sleep(4)
    typing("\nCzeka nas fajna przygoda, poznajmy się!")
    time.sleep(2)
    typing("\nJestem V. a Ty?")
    time.sleep(2)

def print_hi():
    name = input("\nWpisz tu swoje imię -> ")
    typing(f'\nSiemka, {name}. Miło mi :)')

def do_you_like_dragons():
    typing("\nPozwól, że zapytam...")
    time.sleep(2)
    typing("\nLubisz smoki?")
    time.sleep(2)
    typing("\nOdpowiedz 'tak' lub 'nie'")
    time.sleep(2)

def dragon_or_skeleton():
    answer = input("-> ")
    if answer == 'tak':
        typing("\nNo to pacz....")
        time.sleep(2)
        typing("\n...")
        time.sleep(2)
        typing("\n..")
        time.sleep(2)
        typing("\n.")
        time.sleep(2)
        typing("\nNADLATUJE!!!!")
        time.sleep(2)
        print(
            """                                                                                                                      
                                                                                                ░░░▒░░░░░░                                                        
                                                         ░░░░░░░             ▒      ▒░         ▒▒▒▒     ░▒▒░░░░░░░                                                
                                                 ░░░░░▒▒░░░░░ ░░░░░░░▒░      ▒▒     █          ▒▒▒ ▒ ▒░░        ▒▒▒▒▒▒░                                           
                                              ░░░░░░░           ░░░░░█░      ░▓    █▓          ▓▒  ░▒▓ ░▒▓  ░▓▒░░░░░░▒▓█▒░░░                                      
                                         ░░░░░░▒▒
                                         ▒▒▒░░▒▒▒▒░░░░░▒     █       ▒▒  ░▒▓           █░  ▒▓░ ▒ ░▓░▒░▒▒░░░░░     ░▒▓▒                                    
                            ░ ░       ░░▒▒░░░▒▒▒▒░░░░░░░░░ ░░░ ▒▒    ▓      ▒░▒ ░ ▒░▓░  ▒░     ▒░ ░█░ ░▒▒ ░▓░▒ ▒▓▒  ▒▓▒░     ▒█▒░                                 
                                   ░▒▓▒▒  ░░░░░░   ░ ░░░  ░▒░ ░▒▒▒   ░     ░▒ ░░ ░▓░▒  ██         ▒░   ▒▒▓ ▒░▒  ░█▒   ░▓▓░     ░▒▒▓░                              
                                ░░▒▓▒░  ░░░░▒░   ░▒░▒░   ░▒▒  ▒▒ ░░         ░ ░░░▒  ░▒▓▒                ▒▒  ▓░▓   ▓▒░   ░▓█▒      ░▓▓░                            
                               ░▒▒░    ▒░ ▒▒    ░░▒▓     ▒░░  ▒▓            ░  ▒░▒ ░▓░░                 ▓░▒  █░░   ▓▒░    ░██░      ░▓█░                          
                            ░░▒▒░    ░▒░░▒     ▒░▒░     ░▒▒   ▒▒            ░▒ ▒ ░ ▒▒▓░                 ▒░▒  ▒▒░    ▓░▒     ▒▓▒       ░██                         
                           ░░░░     ▒░░▒░    ░▒░▒       ▒▒░  ░░▒            ░░▒   ░▓░▒▓▓▒░              ▒░░░  ▒░░    ▒░▒      ░▓▒       ▓█░                       
                          ▒░░░     ░░░▒     ░▒▒░       ░▒▒   ▒ ▒            ░▒░  ░ ▒░░░ ░▒█░            ▒░ █  ░░▓    ░▒▒░      ░▓░       ░█▓                      
                        ▒▒░░      ▒░░░     ▒░░░        ░▒░    ▒▒▒          ░░▒  ░▒░░░      █▒           ▓ ▒░   ░▒░    ▒▒▓       ░▒░        ▒█▒                    
                      ▒█▒░       ▒░░░     ▒░░          ▒▓      ▒▓           ░░ ░▒ █░░░▒     █▒         ░▒▒░    ░░░     ▒▓        ▒▓░        ░▓▒                   
                     ██         ░▒░       ▒░░          ▒▓      ░▒▒        ▒ ░▒    ░   ░█     █         █░░     ▒▓▒     ░▒▒        ▓▓░        ░▓▒                  
                    █▒          ▓░       ▒░▒           █▒        ▒▒      ▒ ░▒          █     ▓░       ▓▓░      ░█▒      ░▓         ▓▒░         ▒█                 
                  ░█░          █▒        ▒▒            █░        ░░▒                 ░▓      ▒▒      ▒▒▒        █▒      ▒▒▒         ▓▒          ▒█░               
                 ▒█           ▓▓        ▒░▒            ▓░       ░░  ░░             ░█▒       ▓░     ▓░░         █░      ░▒▒          ▓▒          ▒█░              
                ▒▒   ░       ▒▒░        ▒▒             ▓░          ▒ ░▒░        ░▒▓▒        ░█     ▒░ ▒        ░█░       ▒░          ░▒▒          ░█░             
               ▒▒  ░▒       ░▒▒        ░▒░            ░▒▒           ▒░ ▒▒░    ░▓▒░         ░▓    ░░░▒▒▒        ░█░       ░▒▒          ░▒           ░█░            
              ▒░  ░▒░       ▒▒         ▓░░░░░░░        ░░            ▒▒  ░▒░ ░█           ░▒   ░▒▒▒▒           ░▓░    ░▒▒▒▒▓░          ▒░            █▒           
             ░░  ░▒▒       ▒▒░         ▒░▒   ░▒▒▒░    ░▒░             ▒▒    ░█          ▒ ░░░░░░▓▒             ▒█   ░▓▒░  ▒░▓          ▒▓░            █▒          
            ░▒   ▒░▒      ░▒▒          ░▒        ▒▓    ▒░              ▒░  ▒▒▓     ░▒   ▒      ▓░              ▓▓  ▓▒     ▒░▒           ▓▒            ░█▒         
            ▓▓░░▒░░▒░▒ ░▓ ▒▒░          ▒░         ░▓░  ▒▒     ░░░       ▒ ▒▒ ░     ▒░ ░▒▓░▒▒  ▓░       ░░░     █░ ▓░      ░▒▒           ░▓░       ░▓▒░ ░█▒        
                    ░▓ █░ ░░           ▒░           ▓▒ ░▒  ░▒▒▒░▒▒░░    ░▒▓ ▒░    ▒▒  ▓    ▓░ █     ▒▓▒▒░▒▒▒   █░▒░        ▒▒            ▒█      ▓▒      █▒       
                     ▓▒░  ░█▒          ▒░░           ░▒░▒ ▒░          ░▒▒▒░ ▓▒    ▒▒ ░▒     █ ▓   ▒▓░      ░░ ▒█░          ▒▓             █▒    ▒▓        ░       
                      █  ░▒▓           ▒░░             ░▒▓          ░▒░ ░▒░  █     ▒        ▒░▒ ▒▒░           ▒            ▒█             ░█    █                 
                      ▒░ ░▒            ░░░              ▒░        ░░▒  ░░░▒▒ ▒░    ░░ ▒      ▒▒░░                          ▒█              ▓▒  ▒▒                 
                       ▓ ░  ▓          ░▒                         ▓▒▒░░▒    ▒░█     ▒░░  ░░░░▒▒                            ▒▓              ▒▓  ▓░                 
                       ▓  ░█░           ▒░                        █▓▒ ▒░      ▓░   ░░  ▒▒   ░▓                             ▒▒              ░█▒ ▓                  
                       ▓░░▒░            ▓▒                         ▓ ░░       ▒▒   ▒▒░▓▒░░                                 ▒▒               ▒▓ █                  
                       ▒▒ ░ ▒           ▓▓                                    ░▒   ▓▒ ░█▒░                                 ▒▓               ░▒ ▓░                 
                        ▒ ░▒█░          ░█                                    ▒▓   ░   ▒░ ░                               ░▒▒                ▒ ▒░                 
                        ▒ ▒▓░░▒▒▒░      ░█░                                  ▒ ▒         ░█                               ▒░▒                ▓▒▒░                 
                        ░▒█      ░░▒░    ▓░                                 ▒░ ░▒  ░     ▓▒                               ▒▒▒    ░▒░▒▒▒▒▒░   ░█▒░                 
                         █░         ▒▒   ░▒                                ░▒   ░ ▒     ░░░                              ▒░█    ▓▓░     ░▒▒▒  █▒                  
                         ░           ░▓   ▓                                ▒     ▒░    ░  ▒                              ▓░▒   █░          ░▒░█▒                  
                                       ░░ ▒▒                               ▒    ░█     ░ ▒▒                             ░▒▒  ░█              ░█                   
                                        ▓  █░                             ░▒   ░▒▓    ░░░▒▒                             ▒░▒ ░█                                    
                                         ▓ ░█                             ░░  ░▒░░    ▒░▓░▒                            ░▒▒ ░▓                                     
                                          ▒ ▓▒                            ░▒  ▒▒ ▒   ▒░ ▒▒                             ▓▒░░▓                                      
                                           ▒░▓░                            ▒░▓▒ ░▓░  ░░░▒                             ▒▓▒▒▒                                       
                                            ░█▓                              ▒ ░▒░    ░░                              █▓▒░                                        
                                              ▓█░                           ▒  █░  ░░ ░                              ██▒                                          
                                               ░▓░                         ░░░▓░  ▒░  ▓                             ▒█░                                           
                                                                            ▓▓   ░▓  ░█                            ░▓                                             
                                                                           ░▒   ▒▒▒▒▒█                             ░                                              
                                                                          ░▒   ░▒  ░▒                                                                             
                                                                          ▒   ░▒                                                                                  
                                                                         ▓    ▒                                                                                   
                                                                        ░▒   ░░                ░░░  ░░                                                            
                                                                        ▓    ▒              ░░░░▒▒▒░░░░▒░                                                         
                                                                       ░▒   ░░             ▒▒▒░    ░░▒░ ▒░                                                        
                                                                       ░░   ▒             ▒▓░         ░▓ ▒░                                                       
                                                                       ░░   ▒             ▓░            ▓ ▓                                                       
                                                                       ░▒   ▒                           ▒ ▒░                                                      
                                                                        ▓   ▒                           ▒░░░                                                      
                                                                        ▓░  ░▒                          ▓ ▓                                                       
                                                                         ▒   ▒                         ▒ ░▒                                                       
                                                                         ░░   ▒                       ▒ ░░                                                        
                                                                          ▒░  ░▒                    ▒▒░▒░                                                         
                                                                           ▓░   ▒                ░▒▒░▒▓                                                           
                                                                            ▒▒░  ░░░      ░░░▒▒▒▒░░▒▒▒                                                            
                                                                              ░▒░  ░  ░░░░░░░░░░░▒▒░                                                              
                                                                                ░░ ░░░░░░▒▒▒▒▒▒▒░                                                                 
                                                                                      ░░░                                                                                                                                                                                                                                                                                                                                   
            """
        )
    elif answer == 'nie':
        print("To masz szkieleta!!!")
        time.sleep(2)
        print(
        """
                                      _.--""-._
          .                         ."         ".
         / \    ,^.         /(     Y             |      )\
        /   `---. |--'\    (  \__..'--   -   -- -'""-.-'  )
        |        :|    `>   '.     l_..-------.._l      .'
        |      __l;__ .'      "-.__.||_.-'v'-._||`"----"
         \  .-' | |  `              l._       _.'
          \/    | |                   l`^^'^^'j
                | |                _   \_____/     _
                j |               l `--__)-'(__.--' |
                | |               | /`---``-----'"1 |  ,-----.
                | |               )/  `--' '---'   \'-'  ___  `-.
                | |              //  `-'  '`----'  /  ,-'   I`.  \
              _ L |_            //  `-.-.'`-----' /  /  |   |  `. \
             '._' / \         _/(   `/   )- ---' ;  /__.J   L.__.\ :
              `._;/7(-.......'  /        ) (     |  |            | |
              `._;l _'--------_/        )-'/     :  |___.    _._./ ;
                | |                 .__ )-'\  __  \  \  I   1   / /
                `-'                /   `-\-(-'   \ \  `.|   | ,' /
                                   \__  `-'    __/  `-. `---'',-'
                                      )-._.-- (        `-----'
                                     )(  l\ o ('..-.
                               _..--' _'-' '--'.-. |
                        __,,-'' _,,-''            \ \
                       f'. _,,-'                   \ \
                      ()--  |                       \ \
                        \.  |                       /  \
                          \ \                      |._  |
                           \ \                     |  ()|
                            \ \                     \  /
                             ) `-.                   | |
                            // .__)                  | |
                         _.//7'                      | |
                       '---'                         j_| `
                                                    (| |
                                                     |  \
                                                     |lllj
                                                     |||||
        """
    )
    else:
        print("Ymm... Odpowiedz tak lub nie...")
        do_you_like_dragons()






start()
print_hi()
do_you_like_dragons()
dragon_or_skeleton()
