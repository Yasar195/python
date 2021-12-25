import getpass

specials = ['@', '#', '!', '$', '%', '&', '*']
reasons = []
i =0

try:
          password = getpass.getpass()
          if not (not password.islower() and not password.isupper()):
                    reasons.append('cases')
          
          if len(password) <8:
                    reasons.append('length')
          
          for special in specials:
                    if password.__contains__(special):
                              break
                    if special == '*':
                              reasons.append("special")

          for i in range(10):
                    if password.__contains__(str(i)):
                              break
                    elif i == 9:
                              reasons.append('number')

          if len(reasons) == 0:
                    print('password accepted ✔️')
          else:
                    print('password is not accepted ❌ because')
                    for reason in reasons:
                              
                              if reason == 'cases':
                                        print('* it should contain both cases of characters')
                              if reason == 'length':
                                        print('* it must contain atleast 8 characters')
                              if reason == 'special':
                                        print('* it must contain a special character')
                              if reason == 'number':
                                        print('* it must contain numerical characters')
except Exception as error:
          print(error)