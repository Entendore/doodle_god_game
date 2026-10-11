#!/usr/bin/env python3

"""
Doodle God Ultimate Edition
839 elements, 865 combinations, 30 categories
Multi-file architecture: engine in combinations.py, game in this file.
"""

import pygame

import sys

import math

import random



from combinations import ENGINE, ELEMENTS, CATEGORIES, CAT_COLORS, TRIE



pygame.init()



WIDTH, HEIGHT = 1100, 750

FPS = 60



# Colors

BG_DARK = (18, 18, 35)

BG_PANEL = (28, 28, 50)

BG_WORKSPACE = (38, 38, 65)

WHITE = (255, 255, 255)

GOLD = (255, 215, 0)

GRAY = (140, 140, 155)

LGRAY = (200, 200, 215)

DGRAY = (70, 70, 95)

HIGHLIGHT = (90, 130, 255)

GREEN = (70, 210, 110)

RED = (210, 70, 70)

SHADOW = (12, 12, 25)





def draw_shape(surf, shape, color, cx, cy, r):

    """Draw an icon shape."""

    if shape == 0:  # circle

        pygame.draw.circle(surf, color, (cx, cy), max(2, int(r * 0.65)))

    elif shape == 1:  # tri up

        pts = [(cx, cy - r + 2), (cx - r + 2, cy + int(r * 0.6)),

               (cx + r - 2, cy + int(r * 0.6))]

        pygame.draw.polygon(surf, color, pts)

    elif shape == 2:  # tri down

        pts = [(cx, cy + r - 2), (cx - r + 2, cy - int(r * 0.6)),

               (cx + r - 2, cy - int(r * 0.6))]

        pygame.draw.polygon(surf, color, pts)

    elif shape == 3:  # square

        s = int(r * 0.6)

        pygame.draw.rect(surf, color, (cx - s, cy - s, s * 2, s * 2))

    elif shape == 4:  # diamond

        pts = [(cx, cy - r + 2), (cx + r - 2, cy), (cx, cy + r - 2), (cx - r + 2, cy)]

        pygame.draw.polygon(surf, color, pts)

    elif shape == 5:  # hex

        pts = [(cx + int(r * 0.6 * math.cos(math.radians(60 * i - 30))),

                cy + int(r * 0.6 * math.sin(math.radians(60 * i - 30)))) for i in range(6)]

        pygame.draw.polygon(surf, color, pts)

    elif shape == 6:  # star5

        pts = []

        for i in range(5):

            a = math.radians(72 * i - 90)

            pts.append((cx + int(r * 0.7 * math.cos(a)), cy + int(r * 0.7 * math.sin(a))))

            a2 = math.radians(72 * i - 90 + 36)

            pts.append((cx + int(r * 0.3 * math.cos(a2)), cy + int(r * 0.3 * math.sin(a2))))

        pygame.draw.polygon(surf, color, pts)

    elif shape == 7:  # cross

        t = max(2, r // 4)

        pygame.draw.line(surf, color, (cx - r + 2, cy), (cx + r - 2, cy), t)

        pygame.draw.line(surf, color, (cx, cy - r + 2), (cx, cy + r - 2), t)

    elif shape == 8:  # heart

        hs = r * 0.35

        pygame.draw.circle(surf, color, (cx - int(hs * 0.7), cy - int(hs * 0.2)), int(hs))

        pygame.draw.circle(surf, color, (cx + int(hs * 0.7), cy - int(hs * 0.2)), int(hs))

        pygame.draw.polygon(surf, color, [(cx - int(hs * 1.4), cy), (cx, cy + int(r * 0.6)), (cx + int(hs * 1.4), cy)])

    elif shape == 9:  # pentagon

        pts = [(cx + int(r * 0.6 * math.cos(math.radians(72 * i - 90))),

                cy + int(r * 0.6 * math.sin(math.radians(72 * i - 90)))) for i in range(5)]

        pygame.draw.polygon(surf, color, pts)

    elif shape == 10:  # ring

        pygame.draw.circle(surf, color, (cx, cy), int(r * 0.6), max(2, r // 5))

    elif shape == 11:  # crescent

        pygame.draw.circle(surf, color, (cx, cy), int(r * 0.55))

        pygame.draw.circle(surf, tuple(max(0, c - 60) for c in surf.get_at((min(cx + 2, WIDTH - 1), min(cy, HEIGHT - 1)))[:3]) if cx < WIDTH and cy < HEIGHT else BG_DARK,

                         (cx + int(r * 0.25), cy - int(r * 0.1)), int(r * 0.45))

    elif shape == 12:  # bolt

        pts = [(cx + 2, cy - r + 2), (cx - int(r * 0.35), cy + 1), (cx + 1, cy + 1),

               (cx - 2, cy + r - 2), (cx + int(r * 0.35), cy - 1), (cx - 1, cy - 1)]

        pygame.draw.polygon(surf, color, pts)

    elif shape == 13:  # drop

        pygame.draw.circle(surf, color, (cx, cy + int(r * 0.2)), int(r * 0.45))

        pts = [(cx, cy - r + 2), (cx - int(r * 0.45), cy + int(r * 0.05)), (cx + int(r * 0.45), cy + int(r * 0.05))]

        pygame.draw.polygon(surf, color, pts)

    elif shape == 14:  # flame

        pts = [(cx, cy - r + 2), (cx + int(r * 0.5), cy + int(r * 0.4)),

               (cx + int(r * 0.2), cy + int(r * 0.2)), (cx, cy + int(r * 0.7)),

               (cx - int(r * 0.2), cy + int(r * 0.2)), (cx - int(r * 0.5), cy + int(r * 0.4))]

        pygame.draw.polygon(surf, color, pts)

    elif shape == 15:  # leaf

        pygame.draw.ellipse(surf, color, (cx - int(r * 0.3), cy - r, int(r * 0.6), r * 2))

    elif shape == 16:  # paw

        pygame.draw.ellipse(surf, color, (cx - int(r * 0.4), cy + int(r * 0.1), int(r * 0.8), int(r * 0.7)))

        for dx in [-int(r * 0.4), 0, int(r * 0.4)]:

            pygame.draw.circle(surf, color, (cx + dx, cy - int(r * 0.35)), max(2, r // 5))

    elif shape == 17:  # skull

        pygame.draw.circle(surf, color, (cx, cy - int(r * 0.2)), int(r * 0.5))

        pygame.draw.rect(surf, color, (cx - int(r * 0.3), cy + int(r * 0.1), int(r * 0.6), int(r * 0.5)))

    elif shape == 18:  # note

        pygame.draw.circle(surf, color, (cx, cy), int(r * 0.5))

        pygame.draw.line(surf, color, (cx + int(r * 0.3), cy - int(r * 0.3)), (cx + int(r * 0.3), cy + int(r * 0.6)), 2)

    elif shape == 19:  # gear

        pygame.draw.circle(surf, color, (cx, cy), int(r * 0.6))

        pygame.draw.circle(surf, tuple(max(0, c - 40) for c in color), (cx, cy), int(r * 0.25))

        for i in range(6):

            a = math.radians(60 * i)

            x1 = cx + int(r * 0.55 * math.cos(a))

            y1 = cy + int(r * 0.55 * math.sin(a))

            x2 = cx + int(r * 0.85 * math.cos(a))

            y2 = cy + int(r * 0.85 * math.sin(a))

            pygame.draw.line(surf, color, (x1, y1), (x2, y2), max(2, r // 5))

    elif shape == 20:  # atom

        pygame.draw.circle(surf, color, (cx, cy), max(2, r // 5))

        for i in range(3):

            a = math.radians(60 * i)

            pts = [(cx + int(r * 0.8 * math.cos(a + math.radians(t))),

                    cy + int(r * 0.8 * math.sin(a + math.radians(t)))) for t in range(0, 360, 30)]

            pygame.draw.lines(surf, color, False, pts, 1)

    elif shape == 21:  # wave

        pts = [(cx + int(r * 0.9 * math.cos(t / 180 * math.pi * 2) - r * 0.9),

                cy + int(r * 0.3 * math.sin(t / 180 * math.pi * 3))) for t in range(0, 181, 5)]

        if len(pts) > 1:

            pygame.draw.lines(surf, color, False, pts, max(2, r // 5))

    # shapes 22-28 reuse existing shapes with offsets

    elif shape == 22:  # sun (star variant)

        for i in range(8):

            a = math.radians(45 * i)

            pygame.draw.line(surf, color, (cx + int(r * 0.3 * math.cos(a)), cy + int(r * 0.3 * math.sin(a))),

                             (cx + int(r * 0.8 * math.cos(a)), cy + int(r * 0.8 * math.sin(a))), max(1, r // 6))

        pygame.draw.circle(surf, color, (cx, cy), int(r * 0.3))

    elif shape == 23:  # moon (crescent variant)

        pygame.draw.circle(surf, color, (cx, cy), int(r * 0.55))

    elif shape == 24:  # cup

        pygame.draw.rect(surf, color, (cx - int(r*0.3), cy - int(r*0.4), int(r*0.6), int(r*0.7)), border_radius=3)

        pygame.draw.arc(surf, color, (cx - int(r*0.5), cy - int(r*0.3), int(r), int(r*0.5)), 0, math.pi, max(1, r//6))

    elif shape == 25:  # book

        pygame.draw.rect(surf, color, (cx - int(r*0.5), cy - int(r*0.4), int(r), int(r*0.8)), border_radius=2)

        pygame.draw.line(surf, tuple(max(0,c-50) for c in color), (cx, cy - int(r*0.4)), (cx, cy + int(r*0.4)), 1)

    elif shape == 26:  # flag

        pygame.draw.line(surf, color, (cx - int(r*0.4), cy - int(r*0.6)), (cx - int(r*0.4), cy + int(r*0.6)), 2)

        pygame.draw.polygon(surf, color, [(cx - int(r*0.4), cy - int(r*0.6)),

                                          (cx + int(r*0.5), cy - int(r*0.3)),

                                          (cx - int(r*0.4), cy)])

    elif shape == 27:  # crown

        pygame.draw.rect(surf, color, (cx - int(r*0.5), cy, int(r), int(r*0.4)))

        for dx in [-int(r*0.4), 0, int(r*0.4)]:

            pygame.draw.polygon(surf, color, [(cx+dx-int(r*0.15), cy), (cx+dx, cy-int(r*0.5)), (cx+dx+int(r*0.15), cy)])

    elif shape == 28:  # hand

        pygame.draw.circle(surf, color, (cx, cy + int(r*0.2)), int(r*0.4))

        for dx in [-int(r*0.3), -int(r*0.1), int(r*0.1), int(r*0.3)]:

            pygame.draw.line(surf, color, (cx+dx, cy - int(r*0.1)), (cx+dx, cy - int(r*0.6)), max(1, r//5))





def draw_element_icon(surface, name, cx, cy, radius):

    info = ELEMENTS[name]

    bg = info["bg"]

    ic = info["icon"]

    shape = info["shape"]

    r = radius

    pygame.draw.circle(surface, SHADOW, (cx + 2, cy + 2), r)

    pygame.draw.circle(surface, bg, (cx, cy), r)

    inner = tuple(min(c + 25, 255) for c in bg)

    pygame.draw.circle(surface, inner, (cx, cy), r - 2)

    draw_shape(surface, shape, ic, cx, cy, r - 4)

    pygame.draw.circle(surface, tuple(min(c + 50, 255) for c in bg), (cx, cy), r, 2)





class Particle:

    def __init__(self, x, y, color):

        self.x, self.y = x, y

        self.color = color

        self.vx = random.uniform(-4, 4)

        self.vy = random.uniform(-6, -1)

        self.life = random.randint(20, 50)

        self.max_life = self.life

        self.size = random.randint(2, 5)



    def update(self):

        self.x += self.vx

        self.y += self.vy

        self.vy += 0.12

        self.life -= 1



    def draw(self, surface):

        a = max(0, self.life / self.max_life)

        c = tuple(int(v * a) for v in self.color)

        pygame.draw.circle(surface, c, (int(self.x), int(self.y)), max(1, int(self.size * a)))





class DiscoveryAnim:

    def __init__(self, name, x, y):

        self.name, self.x, self.y = name, x, y

        self.timer, self.max_t = 0, 90

        self.particles = [Particle(x, y, ELEMENTS[name]["icon"]) for _ in range(25)]



    def update(self):

        self.timer += 1

        for p in self.particles:

            p.update()

        self.particles = [p for p in self.particles if p.life > 0]



    def draw(self, surface, font):

        for p in self.particles:

            p.draw(surface)

        p = self.timer / self.max_t

        if p < 0.7:

            scale, alpha = min(1.0, p * 3), min(255, int(p * 4 * 255))

        else:

            scale, alpha = 1.0, int((1.0 - (p - 0.7) / 0.3) * 255)

        if scale > 0.15 and alpha > 5:

            rad = int(35 * scale)

            draw_element_icon(surface, self.name, self.x, self.y, rad)

            if p > 0.2:

                t = font.render(self.name, True, GOLD)

                t.set_alpha(min(alpha, 255))

                surface.blit(t, (self.x - t.get_width() // 2, self.y + rad + 8))

                if p > 0.35:

                    t2 = font.render("NEW!", True, GREEN)

                    t2.set_alpha(min(alpha, 255))

                    surface.blit(t2, (self.x - t2.get_width() // 2, self.y + rad + 26))



    def done(self):

        return self.timer >= self.max_t





class FailAnim:

    def __init__(self, x, y):

        self.x, self.y, self.timer, self.max_t = x, y, 0, 45



    def update(self):

        self.timer += 1



    def draw(self, surface, font):

        p = self.timer / self.max_t

        if p < 1:

            t = font.render("Nothing happened...", True, RED)

            t.set_alpha(int((1 - p) * 255))

            surface.blit(t, (self.x - t.get_width() // 2, self.y))



    def done(self):

        return self.timer >= self.max_t





class DoodleGodGame:

    def __init__(self):

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

        pygame.display.set_caption(f"Doodle God Ultimate - {len(ELEMENTS)} Elements")

        self.clock = pygame.time.Clock()

        self.font_lg = pygame.font.SysFont("DejaVu Sans", 34, bold=True)

        self.font_md = pygame.font.SysFont("DejaVu Sans", 20)

        self.font_sm = pygame.font.SysFont("DejaVu Sans", 15)

        self.font_xs = pygame.font.SysFont("DejaVu Sans", 12)

        self.discovered = {"Earth", "Water", "Fire", "Air"}

        self.selected = None

        self.hovered = None

        self.R = 28

        self.SZ = 64

        self.PANEL_Y = 490

        self.scroll = 0

        self.animations = []

        self.search_text = ""

        self.search_active = False

        self.filter_cat = -1

        self.cat_scroll = 0  # horizontal scroll for category bar

        self.hint_text = ""

        self.hint_timer = 0

        self.stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT),

                       random.uniform(0.3, 1)) for _ in range(100)]

        self.search_cursor_timer = 0



    def get_filtered(self):

        elems = [e for e in ELEMENTS if e in self.discovered]

        if self.filter_cat >= 0:

            elems = [e for e in elems if ELEMENTS[e]["cat"] == self.filter_cat]

        if self.search_text:

            # Use Trie for prefix search

            matches = set(TRIE.search_prefix(self.search_text))

            # Also support substring match as fallback

            if not matches:

                q = self.search_text.lower()

                matches = {e for e in elems if q in e.lower()}

            elems = [e for e in elems if e in matches]

        return elems



    def get_per_row(self):

        return (WIDTH - 20) // self.SZ



    def get_elem_center(self, idx, elems):

        pr = self.get_per_row()

        row, col = idx // pr, idx % pr

        x = 10 + col * self.SZ + self.SZ // 2

        y = self.PANEL_Y + 18 + row * self.SZ + self.SZ // 2 - self.scroll

        return x, y



    def total_height(self, elems):

        pr = self.get_per_row()

        rows = max(1, (len(elems) + pr - 1) // pr)

        return rows * self.SZ



    def try_combine(self, e1, e2):

        result = ENGINE.try_combine(e1, e2)

        if result and result not in self.discovered:

            self.discovered.add(result)

            cx, cy = WIDTH // 2, (self.PANEL_Y + 80) // 2 + 200

            self.animations.append(DiscoveryAnim(result, cx, cy))

            return True

        else:

            cx, cy = WIDTH // 2, (self.PANEL_Y + 80) // 2 + 200

            self.animations.append(FailAnim(cx, cy))

            return False



    def run(self):

        running = True

        while running:

            mx, my = pygame.mouse.get_pos()

            elems = self.get_filtered()

            self.hovered = None

            if my > self.PANEL_Y + 18:

                for i in range(len(elems)):

                    cx, cy = self.get_elem_center(i, elems)

                    if math.hypot(mx - cx, my - cy) <= self.R + 4:

                        self.hovered = elems[i]

                        break



            for ev in pygame.event.get():

                if ev.type == pygame.QUIT:

                    running = False

                elif ev.type == pygame.MOUSEBUTTONDOWN:

                    if ev.button == 1:

                        # Search bar

                        sb_rect = pygame.Rect(10, self.PANEL_Y - 22, 220, 22)

                        if sb_rect.collidepoint(mx, my):

                            self.search_active = True

                            continue

                        else:

                            self.search_active = False

                        # Category bar click (scrollable)

                        cat_bar_rect = pygame.Rect(240, self.PANEL_Y - 24, WIDTH - 250, 24)

                        if cat_bar_rect.collidepoint(mx, my):

                            bx = 240 - self.cat_scroll

                            by = self.PANEL_Y - 22

                            for ci, cn in enumerate(CATEGORIES):

                                w = self.font_xs.size(cn)[0] + 10

                                r = pygame.Rect(bx, by, w, 20)

                                if r.collidepoint(mx, my):

                                    self.filter_cat = -1 if ci == 0 else ci - 1

                                    self.scroll = 0

                                    break

                                bx += w + 3

                            else:

                                # If "All" was not found in view, check it

                                self.filter_cat = -1

                                self.scroll = 0

                            continue

                        # Element click

                        if self.hovered:

                            if self.selected is None:

                                self.selected = self.hovered

                            elif self.selected == self.hovered:

                                self.selected = None

                            else:

                                self.try_combine(self.selected, self.hovered)

                                self.selected = None

                        elif my < self.PANEL_Y:

                            self.selected = None

                    elif ev.button == 4:

                        if my > self.PANEL_Y:

                            self.scroll = max(0, self.scroll - 40)

                        elif my > self.PANEL_Y - 30:

                            self.cat_scroll = max(0, self.cat_scroll - 30)

                    elif ev.button == 5:

                        if my > self.PANEL_Y:

                            mh = self.total_height(elems)

                            vis = HEIGHT - self.PANEL_Y - 18

                            self.scroll = min(max(0, mh - vis), self.scroll + 40)

                        elif my > self.PANEL_Y - 30:

                            self.cat_scroll += 30

                elif ev.type == pygame.MOUSEWHEEL:

                    if my > self.PANEL_Y:

                        self.scroll -= ev.y * 35

                        mh = self.total_height(elems)

                        vis = HEIGHT - self.PANEL_Y - 18

                        self.scroll = max(0, min(max(0, mh - vis), self.scroll))

                    elif my > self.PANEL_Y - 30:

                        self.cat_scroll = max(0, self.cat_scroll - ev.y * 30)

                elif ev.type == pygame.KEYDOWN:

                    if self.search_active:

                        if ev.key == pygame.K_BACKSPACE:

                            self.search_text = self.search_text[:-1]

                        elif ev.key == pygame.K_RETURN:

                            self.search_active = False

                        elif ev.key == pygame.K_ESCAPE:

                            self.search_active = False

                        elif ev.unicode and len(self.search_text) < 30:

                            self.search_text += ev.unicode

                    else:

                        if ev.key == pygame.K_ESCAPE:

                            self.selected = None

                        elif ev.key == pygame.K_h:

                            hint = ENGINE.get_hint(self.discovered)

                            if hint:

                                a, b, r = hint

                                self.hint_text = f"Hint: {a} + {b} = ?"

                            else:

                                self.hint_text = "All discovered!"

                            self.hint_timer = 180



            self.search_cursor_timer = (self.search_cursor_timer + 1) % 60

            if self.hint_timer > 0:

                self.hint_timer -= 1



            for a in self.animations:

                a.update()

            self.animations = [a for a in self.animations if not a.done()]



            # ── DRAW ──

            self.screen.fill(BG_DARK)

            for sx, sy, sb in self.stars:

                c = tuple(int(v * sb) for v in (130, 140, 180))

                pygame.draw.circle(self.screen, c, (sx, sy), 1 if sb < 0.7 else 2)



            # Top bar

            pygame.draw.rect(self.screen, BG_PANEL, (0, 0, WIDTH, 60))

            pygame.draw.line(self.screen, HIGHLIGHT, (0, 60), (WIDTH, 60), 2)

            t = self.font_lg.render("Doodle God", True, GOLD)

            self.screen.blit(t, (15, 10))

            t2 = self.font_sm.render(f"{len(ELEMENTS)} Elements  |  {len(self.discovered)} discovered", True, GRAY)

            self.screen.blit(t2, (15, 40))

            total = len(ELEMENTS)

            found = len(self.discovered)

            bx, by, bw, bh = WIDTH - 260, 10, 240, 16

            pygame.draw.rect(self.screen, DGRAY, (bx, by, bw, bh), border_radius=8)

            fw = int(bw * found / total) if total else 0

            if fw > 0:

                pygame.draw.rect(self.screen, GREEN, (bx, by, fw, bh), border_radius=8)

            pygame.draw.rect(self.screen, LGRAY, (bx, by, bw, bh), 1, border_radius=8)

            pct = self.font_xs.render(f"{found}/{total} ({found * 100 // total}%)", True, WHITE)

            self.screen.blit(pct, (bx + bw // 2 - pct.get_width() // 2, by + 1))

            hb = pygame.Rect(WIDTH - 80, 36, 65, 22)

            pygame.draw.rect(self.screen, (50, 40, 80), hb, border_radius=6)

            pygame.draw.rect(self.screen, GOLD, hb, 1, border_radius=6)

            ht = self.font_xs.render("Hint (H)", True, GOLD)

            self.screen.blit(ht, (hb.x + hb.w // 2 - ht.get_width() // 2, hb.y + 4))



            # Workspace

            ws = pygame.Rect(8, 66, WIDTH - 16, self.PANEL_Y - 74)

            pygame.draw.rect(self.screen, BG_WORKSPACE, ws, border_radius=10)

            pygame.draw.rect(self.screen, DGRAY, ws, 1, border_radius=10)

            if self.selected and not self.hovered:

                info = ELEMENTS[self.selected]

                cx = WIDTH // 2

                cy = ws.centery + 20

                draw_element_icon(self.screen, self.selected, cx, cy, 38)

                nt = self.font_sm.render(self.selected, True, WHITE)

                self.screen.blit(nt, (cx - nt.get_width() // 2, cy + 44))

                # Show possible combos for selected element

                partners = ENGINE.all_combos_for(self.selected, self.discovered)

                if partners:

                    combo_text = "Combos: " + ", ".join(f"{p}->{r}" for p, r in partners[:5])

                    if len(partners) > 5:

                        combo_text += f" (+{len(partners)-5} more)"

                    ct = self.font_xs.render(combo_text, True, HIGHLIGHT)

                    self.screen.blit(ct, (WIDTH // 2 - ct.get_width() // 2, ws.y + 12))

                ht2 = self.font_md.render(f"Selected: {self.selected} - click another!", True, HIGHLIGHT)

                self.screen.blit(ht2, (WIDTH // 2 - ht2.get_width() // 2, ws.y + 30))

            elif not self.selected:

                ht3 = self.font_md.render("Click two elements below to combine them!", True, GRAY)

                self.screen.blit(ht3, (WIDTH // 2 - ht3.get_width() // 2, ws.centery - 10))



            # Animations

            for a in self.animations:

                a.draw(self.screen, self.font_md)



            # Hint toast

            if self.hint_timer > 0 and self.hint_text:

                alpha = min(255, self.hint_timer * 4)

                ht_surf = self.font_md.render(self.hint_text, True, GOLD)

                ht_surf.set_alpha(alpha)

                self.screen.blit(ht_surf, (WIDTH // 2 - ht_surf.get_width() // 2, ws.y + 60))



            # Completion

            if len(self.discovered) == total:

                ct = self.font_lg.render("You discovered everything!", True, GOLD)

                self.screen.blit(ct, (WIDTH // 2 - ct.get_width() // 2, ws.centery - 18))



            # Bottom panel

            panel_bg = pygame.Rect(0, self.PANEL_Y - 30, WIDTH, HEIGHT - self.PANEL_Y + 30)

            pygame.draw.rect(self.screen, BG_PANEL, panel_bg)

            pygame.draw.line(self.screen, HIGHLIGHT, (0, self.PANEL_Y - 30), (WIDTH, self.PANEL_Y - 30), 2)



            # Search bar

            sb_rect = pygame.Rect(10, self.PANEL_Y - 22, 220, 22)

            sc = HIGHLIGHT if self.search_active else DGRAY

            pygame.draw.rect(self.screen, sc, sb_rect, border_radius=4)

            pygame.draw.rect(self.screen, LGRAY, sb_rect, 1, border_radius=4)

            cursor = "|" if self.search_active and self.search_cursor_timer < 30 else ""

            st = self.font_xs.render(f"Search: {self.search_text}{cursor}", True, WHITE)

            self.screen.blit(st, (sb_rect.x + 5, sb_rect.y + 4))



            # Category bar (scrollable for 30 categories)

            cat_bar = pygame.Rect(240, self.PANEL_Y - 24, WIDTH - 250, 24)

            self.screen.set_clip(cat_bar)

            bx = 240 - self.cat_scroll

            for ci, cn in enumerate(CATEGORIES):

                w = self.font_xs.size(cn)[0] + 10

                active = (self.filter_cat == -1 and ci == 0) or (self.filter_cat == ci - 1)

                bg_c = HIGHLIGHT if active else DGRAY

                cc = CAT_COLORS[ci] if ci < len(CAT_COLORS) else GRAY

                if active:

                    bg_c = cc

                r = pygame.Rect(bx, self.PANEL_Y - 22, w, 20)

                pygame.draw.rect(self.screen, bg_c, r, border_radius=4)

                tc = WHITE if active else GRAY

                tt = self.font_xs.render(cn, True, tc)

                self.screen.blit(tt, (r.x + r.w // 2 - tt.get_width() // 2, r.y + 3))

                bx += w + 3

            self.screen.set_clip(None)



            # Scroll indicator for category bar

            max_cat_w = sum(self.font_xs.size(cn)[0] + 10 for cn in CATEGORIES) + 3 * (len(CATEGORIES) - 1)

            if max_cat_w > cat_bar.width:

                indicator_w = max(20, int(cat_bar.width * cat_bar.width / max_cat_w))

                indicator_x = cat_bar.x + int(self.cat_scroll / max_cat_w * cat_bar.width)

                pygame.draw.rect(self.screen, DGRAY, (indicator_x, self.PANEL_Y - 2, indicator_w, 3), border_radius=2)



            # Element grid

            clip = pygame.Rect(0, self.PANEL_Y + 16, WIDTH, HEIGHT - self.PANEL_Y - 16)

            self.screen.set_clip(clip)

            elems = self.get_filtered()

            for i, ename in enumerate(elems):

                cx, cy = self.get_elem_center(i, elems)

                if cy < self.PANEL_Y + 10 or cy > HEIGHT + 10:

                    continue

                is_sel = (self.selected == ename)

                is_hov = (self.hovered == ename)

                if is_sel:

                    gs = pygame.Surface((self.R * 2 + 14, self.R * 2 + 14), pygame.SRCALPHA)

                    pygame.draw.circle(gs, (*HIGHLIGHT, 90), (self.R + 7, self.R + 7), self.R + 7)

                    self.screen.blit(gs, (cx - self.R - 7, cy - self.R - 7))

                if is_hov and not is_sel:

                    gs = pygame.Surface((self.R * 2 + 10, self.R * 2 + 10), pygame.SRCALPHA)

                    pygame.draw.circle(gs, (*WHITE, 50), (self.R + 5, self.R + 5), self.R + 5)

                    self.screen.blit(gs, (cx - self.R - 5, cy - self.R - 5))

                draw_element_icon(self.screen, ename, cx, cy, self.R)

                if is_sel:

                    pygame.draw.circle(self.screen, GOLD, (cx, cy), self.R + 2, 2)

                nt = self.font_xs.render(ename, True, GOLD if is_hov else LGRAY)

                self.screen.blit(nt, (cx - nt.get_width() // 2, cy + self.R + 2))

            self.screen.set_clip(None)



            # Scrollbar

            th = self.total_height(elems)

            vis = HEIGHT - self.PANEL_Y - 18

            if th > vis:

                sb_h = max(20, int(vis * vis / th))

                sb_y = self.PANEL_Y + 18 + int(self.scroll / th * vis)

                pygame.draw.rect(self.screen, DGRAY, (WIDTH - 8, sb_y, 5, sb_h), border_radius=3)



            pygame.display.flip()

            self.clock.tick(FPS)

        pygame.quit()

        sys.exit()





if __name__ == "__main__":

    game = DoodleGodGame()

    game.run()
