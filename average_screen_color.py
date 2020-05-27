### Code by Anime no Sekai
###
###
import pyautogui
import PIL

def average_image_color(image):
	"""
	Code by olooney on GitHub
	> https://gist.github.com/olooney/1246268

	Returns the average color from a given image (PIL)
	"""
	i = image
	h = i.histogram()

	# split into red, green, blue
	r = h[0:256]
	g = h[256:256*2]
	b = h[256*2: 256*3]

	# perform the weighted average of each channel:
	# the *index* is the channel value, and the *value* is its weight
	return [
		sum( i*w for i, w in enumerate(r) ) / sum(r),
		sum( i*w for i, w in enumerate(g) ) / sum(g),
		sum( i*w for i, w in enumerate(b) ) / sum(b)
	]



if __name__ == '__main__':
    import sys
    import numpy as np
    import matplotlib.pyplot as plt
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    if len(sys.argv) > 1:
        refresh_rate = int(sys.argv[1])
    else:
        refresh_rate = 10
    print('Chosen refresh rate: ' + str(refresh_rate))
    plt.ion()

    fig = plt.gcf()
    fig.show()
    fig.canvas.draw()

    iteration = 0
    plt.title('Average Screen Color')

    while True:
        iteration += 1
        image = pyautogui.screenshot()
        rgb = average_image_color(image)

        #VIZUALIZATION
        spikes = np.random.random(1) #To show a rectangle

        plt.xlabel('Average Color (RGB): ' + str(rgb))
        plt.eventplot(spikes, orientation='horizontal', linelengths=0.9, linewidths=1000, color = [(rgb[0]/255, rgb[1]/255, rgb[2]/255)])

        if iteration > refresh_rate:
            iteration = 0
            plt.clf()
            plt.title('Average Screen Color')

        fig.canvas.draw()
        plt.pause(0.000001)

def get_average_screen_color():
    '''
    Returns the current screen average color.
    '''
    image = pyautogui.screenshot()
    rgb = average_image_color(image)
    return rgb