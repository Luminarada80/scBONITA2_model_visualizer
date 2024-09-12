import pygame
import math
from object import Object
import pygame.freetype

class Node(Object):
    def __init__(self, name, position, color):
        super().__init__(name, position, color)

        self.size = self.size
        
        self.inactive_image = pygame.image.load('visualizer/images/node_inactive.png').convert_alpha()
        self.active_image = pygame.image.load('visualizer/images/node_active.png').convert_alpha()

        self.inactive_scaled_image = pygame.transform.smoothscale(self.inactive_image, (self.size, self.size))
        self.active_scaled_image = pygame.transform.smoothscale(self.active_image, (self.size, self.size))

        self.activation_threshold = 1

        self.image = self.inactive_image
        self.rect = self.image.get_rect(center=self.position)
        self.original_image = self.image

        self.font_size = 4
        self.font = pygame.freetype.Font('visualizer/arial.ttf', self.font_size, resolution=200)
        self.font.strength = 0.01

        self.is_node = True

        self.angle = 0

    def draw_circle(self):
        # Clear the image
        if self.state == 0:
            self.image = self.inactive_scaled_image
        elif self.state == 1:
            self.image = self.active_scaled_image

        # Apply rotation if needed
        self.rect = self.image.get_rect(center=self.position)
        
        text_surface, text_rect = self.font.render(self.name, pygame.Color('black'))
        text_rect.center = (self.size/2, self.size/2)
        self.image.blit(text_surface, text_rect)

        if self.name == '':
            activation_surface, activation_rect = self.font.render(str(self.state), pygame.Color('black'))
            activation_rect.center = (self.size/2, self.size/2)
            self.image.blit(activation_surface, activation_rect)

    
    def update_object(self, events, connections, gate_ids, node_ids, uuid_dict, game, keys, mouse_pos):
        self.update_activation_highlight(self.draw_circle)
        self.update(events, connections, gate_ids, node_ids, uuid_dict, self.rect, self.draw_circle, game, keys, mouse_pos)     


