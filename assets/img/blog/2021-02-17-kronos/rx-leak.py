from basalt import *

black = RGB(0x000000)
white = RGB(0xFFFFFF)
red = RGB(0xB85450)
green = RGB(0x82B366)

font = Font('CMU Sans Serif', file='cmunss.ttf')
font_mono = Font('CMU Typewriter Text', file='cmuntt.ttf')
font_big = 16
font_medium = 10
font_small = 8

frame_style = Style({
            Property.stroke_width: 1,
            Property.stroke: black,
            Property.fill_opacity: 0
        })
uninit_bit_style = Style({
    Property.fill: red,
})
init_bit_style = Style({
    Property.fill: green,
})
dead_bit_visible_style = Style({
    Property.fill_opacity: 0.5,
})
invisible_style = Style({
    Property.fill_opacity: 0,
})
visible_style = Style({
    Property.fill_opacity: 1,
})

padding = 5
fig_padding = 5

BITS = 8
FRAMES = 40

def make_frame_norm(frame):
    rx_data_label = Text('rx_data', font_mono, size=font_medium)
    rx_data_frame = Rectangle(style=frame_style)
    uninit_bits = [Text(str(i), font_mono, size=font_big, style=uninit_bit_style) for i in range(BITS if frame < 2 else BITS - 1)]
    init_bit = []
    init_bit_digit = (frame-2)//5
    dead_bit = Text(str(7 - (frame-5)//5),
                    font_mono,
                    size=font_big,
                    style=dead_bit_visible_style if frame % 5 == 2 else invisible_style)

    if frame > 1:
        init_bit.append(Text(str(init_bit_digit), font_mono, size=font_big, style=init_bit_style))

    bits = [Text(str(i), font_mono, size=font_big, style=uninit_bit_style if i > (frame-5)//5 else init_bit_style) for i in range(BITS)]

    lsb = True
    arrow = Text("<" if lsb else ">", font_mono, size=font_big)

    rcvd = (frame+3)//5
    rcvd_count = Text(f"Received: {rcvd}/8", font, size=font_small)

    order_label = Text("Order: " + ("LSB" if lsb else "MSB"), font, size=font_small)

    info_str = ""
    if frame == 0:
        info_str = "Initial state, all bits are old data"
    elif frame == FRAMES-1:
        info_str = "Data leaked to CPU"
    elif frame % 5 == 1 or frame % 5 == 2 or frame % 5 == 3:
        info_str = "New bit received over SPI"
    elif frame % 5 == 4 or frame % 5 == 0:
        info_str = ""

    info_label = Text(info_str, font, size=font_medium, style=visible_style if info_str != "" else invisible_style)

    return Group([rx_data_label, rx_data_frame, dead_bit, arrow, rcvd_count, order_label, info_label] + bits, [
        rx_data_label.bounds.bottom == rx_data_frame.bounds.top - padding,
        rx_data_label.bounds.left == rx_data_frame.bounds.left,

        bits[-1].bounds.left == rx_data_frame.bounds.left + padding,
        bits[0].bounds.right == rx_data_frame.bounds.right - padding,
        *[bits[i].bounds.left == bits[i+1].bounds.right + padding for i in range(len(bits) - 1)],
        *[bit.bounds.top == rx_data_frame.bounds.top + padding - 2 for bit in bits + [dead_bit, arrow]],
        *[bit.bounds.bottom == rx_data_frame.bounds.bottom - padding for bit in bits + [dead_bit, arrow]],
        dead_bit.bounds.right == rx_data_frame.bounds.left - padding if lsb else True,
        dead_bit.bounds.left == rx_data_frame.bounds.right + padding if not lsb else True,
        arrow.bounds.right == rx_data_frame.bounds.left - padding if not lsb else True,
        arrow.bounds.left == rx_data_frame.bounds.right + padding if lsb else True,

        rcvd_count.bounds.top == rx_data_frame.bounds.bottom + padding,
        rcvd_count.bounds.right == rx_data_frame.bounds.right,

        order_label.bounds.top == rx_data_frame.bounds.bottom + padding,
        order_label.bounds.left == rx_data_frame.bounds.left,

        info_label.bounds.bottom == rx_data_label.bounds.top - 2 * padding,
        info_label.bounds.left == rx_data_label.bounds.left - 2 * padding

        # info_label.bounds.top == order_label.bounds.bottom + padding,
        # info_label.bounds.center.x == rx_data_frame.bounds.center.x
    ])

def make_frame_vuln(frame):
    rx_data_label = Text('rx_data', font_mono, size=font_medium)
    rx_data_frame = Rectangle(style=frame_style)
    uninit_bits = [Text(str(i), font_mono, size=font_big, style=uninit_bit_style) for i in range(BITS if frame < 2 else BITS - 1)]
    init_bit = []
    init_bit_digit = (frame-2)//5
    dead_bit = Text("7" if frame < 5 else str((frame-5)//5),
                    font_mono,
                    size=font_big,
                    style=dead_bit_visible_style if frame % 5 == 2 else invisible_style)

    if frame > 1:
        init_bit.append(Text(str(init_bit_digit), font_mono, size=font_big, style=init_bit_style))

    if init_bit_digit % 2 == 0:
        bits = init_bit + uninit_bits
    else:
        bits = uninit_bits + init_bit

    lsb = (frame//5) % 2 == 0
    arrow = Text("<" if lsb else ">", font_mono, size=font_big)

    rcvd = (frame+3)//5
    rcvd_count = Text(f"Received: {rcvd}/8", font, size=font_small)

    order_label = Text("Order: " + ("LSB" if lsb else "MSB"), font, size=font_small)

    info_str = ""
    if frame == 0:
        info_str = "Initial state, all bits are old data"
    elif frame == FRAMES-1:
        info_str = "Data leaked to CPU"
    elif frame % 5 == 1 or frame % 5 == 2 or frame % 5 == 3:
        info_str = "New bit received over SPI"
    elif frame % 5 == 4 or frame % 5 == 0:
        info_str = "CPU flips order"

    info_label = Text(info_str, font, size=font_medium, style=visible_style if info_str != "" else invisible_style)

    return Group([rx_data_label, rx_data_frame, dead_bit, arrow, rcvd_count, order_label, info_label] + bits, [
        rx_data_label.bounds.bottom == rx_data_frame.bounds.top - padding,
        rx_data_label.bounds.left == rx_data_frame.bounds.left,

        bits[-1].bounds.left == rx_data_frame.bounds.left + padding,
        bits[0].bounds.right == rx_data_frame.bounds.right - padding,
        *[bits[i].bounds.left == bits[i+1].bounds.right + padding for i in range(len(bits) - 1)],
        *[bit.bounds.top == rx_data_frame.bounds.top + padding - 2 for bit in bits + [dead_bit, arrow]],
        *[bit.bounds.bottom == rx_data_frame.bounds.bottom - padding for bit in bits + [dead_bit, arrow]],
        dead_bit.bounds.right == rx_data_frame.bounds.left - padding if lsb else True,
        dead_bit.bounds.left == rx_data_frame.bounds.right + padding if not lsb else True,
        arrow.bounds.right == rx_data_frame.bounds.left - padding if not lsb else True,
        arrow.bounds.left == rx_data_frame.bounds.right + padding if lsb else True,

        rcvd_count.bounds.top == rx_data_frame.bounds.bottom + padding,
        rcvd_count.bounds.right == rx_data_frame.bounds.right,

        order_label.bounds.top == rx_data_frame.bounds.bottom + padding,
        order_label.bounds.left == rx_data_frame.bounds.left,

        info_label.bounds.bottom == rx_data_label.bounds.top - 2 * padding,
        info_label.bounds.left == rx_data_label.bounds.left - 2 * padding

        # info_label.bounds.top == order_label.bounds.bottom + padding,
        # info_label.bounds.center.x == rx_data_frame.bounds.center.x
    ])

def canvas_wrap(frame):
    width = Variable()
    height = Variable()
    g = frame
    top = Group([g], [
        g.bounds.left == fig_padding,
        g.bounds.top == fig_padding,
        g.bounds.width == width - 2*fig_padding,
        g.bounds.height == height - 2*fig_padding,
    ])
    return Canvas(top, width=width, height=height, color=white)

frames = [canvas_wrap(make_frame_norm(i)) for i in range(FRAMES)]
frames_no_canvas = [make_frame(i) for i in range(FRAMES)]

g = Group(frames_no_canvas, [
    *[frames_no_canvas[i].bounds.left == frames_no_canvas[i+1].bounds.left for i in range(FRAMES-1)],
    *[frames_no_canvas[i].bounds.bottom == frames_no_canvas[i+1].bounds.top - 3*padding for i in range(FRAMES-1)]
    ])


width = Variable()
height = Variable()

top = Group([g], [
    g.bounds.left == fig_padding,
    g.bounds.top == fig_padding,
    g.bounds.width == width - 2*fig_padding,
    g.bounds.height == height - 2*fig_padding,
])
c = Canvas(top, width=width, height=height)
