B


    ���]�  �               @   s�   d dl Z d dlZd dlZd dlmZ eedd�� eedd�� eedd�� eedd�� eedd	�� eed
d��Zeedd
��Zdd� Ze�  dd� Z	e	�  dd� Z
e
�  dS )�    N)�coloredz-============WELCOME TO BANgLADESH============�greenz               ===============z                  BANgLADESHz                     V1.Oz
 URL WITH http/https:ZyellowzTarget URL: �redzJ
 (1) Get Sources:
 (2) Get Response 
 (3) Get Cookies (If Available)
 >> Zbluec              C   sH   t �t�} tdd�}d| _tdkrDt|�t| j	��� tt
dd�� d S )Nz./LastUrl-Source.txt�wz
ISO-8859-1�1z2Successfully Cracked ! 
 Check LastUrl-Source.txt r   )�requests�get�inp�open�encoding�x�print�write�str�textr   )�sZsources� r   �O/data/data/com.termux/files/home/storage/downloads/myscriptPYTHON.PY/payload.py�source   s    

r   c              C   s(   t �t�} tdkr$ttdd�| j� d S )N�2zRespond code: r   )r   r   r	   r   r
   r   Zstatus_code)Zgettr   r   r   r      s    
r   c              C   sd   t �t�} tdd�}d| _tdkrHt|�t| j	�
� ��� ttdd�� tdkr`t�
tdd	�� d S )
Nz
./Cookies.txtr   z
ISO-8859-1�3z3Successfully Cracked Cookies ! 
 Check Cookies.txt r   �exitzShutting down...r   )r   r   r	   r
   r   r   r
   r   r   ZcookiesZget_dictr   �sysr   )�kZcookiedr   r   r   �cookie   s    

r   )r   r   Z	termcolorr   r
   �inputr	   r   r   r   r   r   r   r   r   �<module>   s   	
