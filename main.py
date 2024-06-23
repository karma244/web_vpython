#Web VPython 3.2 < 실사용 시 주석이 없어야 작동
scene.title = '<b style="font-size:50px">s키=멈춤, j키=오브젝트 점프, r키=다시 시작</b>' #html 버전이 낮은지 inline style값에 margin, padding 등을 추가해봤지만 작동하지 않았음.
scene.caption = '<b style="font-size:20px">숨겨진 이스터에그가 있습니다. 찾아보세요.</b>'
scene.height = 760 #main scene 높이
scene.width = 1840 #main scene 너비
scene.range = 30 #main scene 확대 or 축소
all = group(pos=vec(0,0,0)) #group method로 오브젝트를 묶어서 병렬 처리할 수 있음.
easter = group()

hat = ring(group=all,pos=vec(0, 0, 0), axis=vec(0, 1, 0), radius = 2, thickness = 5, color=color.white)
headp = shapes.ellipse(group=all,height=5, width=4)
sphere(group=all, pos=vec(4.3, 0, 0), radius=3, color=color.red)
sphere(group=all, pos=vec(-4.3, 0, 0), radius=3, color=color.red)
sphere(group=all, pos=vec(0, 0, 4.3), radius=3, color=color.red)
sphere(group=all, pos=vec(0, 0, -4.3), radius=3, color=color.red)
eye =  ellipsoid(group=all,pos=vec(-1.3, -6, 2), length=0.7, height=1.3, width=0.5, color=color.black)
eye =  ellipsoid(group=all,pos=vec(1.3, -6, 2), length=0.7, height=1.3, width=0.5, color=color.black)
semicircle = extrusion(group=all,shape=[headp, shapes.circle(pos=[0,-2.6],radius=1.5,angle1=0,angle2=-pi)], path=[vec(0,-5,2),vec(0,-5,-2)], color=vec(1, 0.855, 0.741))
t = text(text='Congratulations!!!!!!!', align='center', color=color.white, font='serif')
'''
^^^^^^^^^^^^^^^^^
윗 부분은 오브젝트 디자인 관련 코드임. (마리오의 키노피오를 참고하여 디자인 함.)
'''


def move(): #y=sinx 함수의 그래프를 따라 오브젝트가 움직임. 
    dt = 0.1
    while True:
        k = keysdown()
        if 's' in k:
            break
        if all.pos.x >= 12*pi:
            all.pos.x = -12*pi
        rate(60) #화면 재생 빈도인데, 값이 클수록 빠름
        all.pos.x = all.pos.x + dt
        all.pos.y = 3*sin(all.pos.x)

t.visible = False
move()
dt = 5
while True:
    rate(30)
    k = keysdown()
    a = 0
    if 'r' in k:
        move()
    elif 'j' in k:
        while all.pos.y <= 10:
            if dt > 1:
                dt = dt * 0.5
            rate(60)
            all.pos.y = all.pos.y + dt
        dt = 3
        while all.pos.y >= 0:
            rate(30)
            dt = dt * 1.1
            all.pos.y = all.pos.y - dt
    elif 'e' in k:
        all.visible = False
        t.visible = True
        scene.range=10 #3D text object는 크기 조정하는 방법을 몰라서 main scene range값을 낮춤
        while True:
            a = a + 0.05
            if a >= 4*pi:
                break
            rate(30)
            t.rotate(angle=0.05, axis=vec(0,1,0))
        all.visible = True
        scene.range=30
        t.visible = False
