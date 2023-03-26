#!/usr/bin/env python
# coding: utf-8

# In[10]:


# Importação bibliotecas

import cv2
import numpy as np
import pyautogui

# Definindo o formato do video, codec do video e o nome do arquivo

SCREEN_SIZE = (1920, 1080)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("gravacao.avi", fourcc, 20.0, (SCREEN_SIZE))

# Definição da Captura da tela e da gravação da tela

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
        
# Encerrando o processo de gravação

cv2.destroyAllWindows()
out.release()


# In[ ]:




