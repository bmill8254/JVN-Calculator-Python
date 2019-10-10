import math
import time

print("-----------------------------------------------------------------")
print("|Single Speed Gearbox Calculation V1.6 Created by Brandon Miller|")
print("-----------------------------------------------------------------")

while True:

    while True:
        DECIDE = str(input("Mechanism(DT/ARM/ELV/INT): "))
#########################Drivetrain Calculation################################

        if DECIDE == 'DT':
            while True:
                mtr = str(input("Motor Type(CIM/MCIM/775/BAG): "))

                if mtr == 'CIM':
                    break
                elif mtr == 'MCIM':
                    break
                elif mtr == '775':
                    break
                elif mtr == 'BAG':
                    break
                else:
                    print("Invalid Input. Please Try Again.")
                    continue

            m = str(mtr)
            GearboxCount = input("Number of Gearboxes: ")
            gc = float(GearboxCount)
            MotorCount = input("Number of Motors Per Gearbox: ")
            mc = float(MotorCount)
            Weight = input("Robot Weight: ")
            w = float(Weight)
            WheelDiameter = input("Wheel Diameter: ")
            wd = float(WheelDiameter)
            CoeffFriction = input("Coefficent of Friction (If unknown use 1.0): ")
            cf = float(CoeffFriction)

            stage = input("Number of Stages: ")
            s = float(stage)

            if s == 1:
                DRIVE1 = input("Driving Gear 1: ")
                DRIVEN1 = input("Driven Gear 1: ")
                DR1 = float(DRIVE1)
                DV1 = float(DRIVEN1)
                DRIVE2 = 1
                DRIVEN2 = 1
                DR2 = float(DRIVE2)
                DV2 = float(DRIVEN2)
                DRIVE3 = 1
                DRIVEN3 = 1
                DR3 = float(DRIVE3)
                DV3 = float(DRIVEN3)
                DRIVE4 = 1
                DRIVEN4 = 1
                DR4 = float(DRIVE4)
                DV4 = float(DRIVEN4)
            elif s == 2:
                DRIVE1 = input("Driving Gear 1: ")
                DRIVEN1 = input("Driven Gear 1: ")
                DR1 = float(DRIVE1)
                DV1 = float(DRIVEN1)
                DRIVE2 = input("Driving Gear 2: ")
                DRIVEN2 = input("Driven Gear 2: ")
                DR2 = float(DRIVE2)
                DV2 = float(DRIVEN2)
                DRIVE3 = 1
                DRIVEN3 = 1
                DR3 = float(DRIVE3)
                DV3 = float(DRIVEN3)
                DRIVE4 = 1
                DRIVEN4 = 1
                DR4 = float(DRIVE4)
                DV4 = float(DRIVEN4)
            elif s == 3:
                DRIVE1 = input("Driving Gear 1: ")
                DRIVEN1 = input("Driven Gear 1: ")
                DR1 = float(DRIVE1)
                DV1 = float(DRIVEN1)
                DRIVE2 = input("Driving Gear 2: ")
                DRIVEN2 = input("Driven Gear 2: ")
                DR2 = float(DRIVE2)
                DV2 = float(DRIVEN2)
                DRIVE3 = input("Driving Gear 3: ")
                DRIVEN3 = input("Driven Gear 3: ")
                DR3 = float(DRIVE3)
                DV3 = float(DRIVEN3)
                DRIVE4 = 1
                DRIVEN4 = 1
                DR4 = float(DRIVE4)
                DV4 = float(DRIVEN4)
            elif s == 4:
                DRIVE1 = input("Driving Gear 1: ")
                DRIVEN1 = input("Driven Gear 1: ")
                DR1 = float(DRIVE1)
                DV1 = float(DRIVEN1)
                DRIVE2 = input("Driving Gear 2: ")
                DRIVEN2 = input("Driven Gear 2: ")
                DR2 = float(DRIVE2)
                DV2 = float(DRIVEN2)
                DRIVE3 = input("Driving Gear 3: ")
                DRIVEN3 = input("Driven Gear 3: ")
                DR3 = float(DRIVE3)
                DV3 = float(DRIVEN3)
                DRIVE4 = input("Driving Gear 4: ")
                DRIVEN4 = input("Driven Gear 4: ")
                DR4 = float(DRIVE4)
                DV4 = float(DRIVEN4)

            r1 = (DV1/DR1)
            r2 = (DV2/DR2)
            r3 = (DV3/DR3)
            r4 = (DV4/DR4)
            rO = (r1*r2*r3*r4)
            rOr = round(rO, 2)
            rT = ((DR1/DV1)*(DR2/DV2)*(DR3/DV3)*(DR4/DV4))

            if m == 'CIM':
                RPM = 5330
                ST = 2.41
                SC = 131
                FC = 2.7

                print ("-------------------")
                time.sleep(0.1)
                print ("Motor: CIM")
                time.sleep(0.1)
                print ("Free Speed:",RPM,"RPM")
                time.sleep(0.1)
                print ("Stall Torque:",ST)
                time.sleep(0.1)
                print ("Stall Current:",SC,"AMPS")
                time.sleep(0.1)
                print ("Free Current:",FC,"AMPS")
                time.sleep(0.1)
                print ("-------------------")

            elif m == 'MCIM':
                RPM = 5840
                ST = 1.41
                SC = 89
                FC = 3

                print ("-------------------")
                time.sleep(0.1)
                print ("Motor: MINI CIM")
                time.sleep()
                print ("Free Speed:",RPM,"RPM")
                time.sleep(0.1)
                print ("Stall Torque:",ST)
                time.sleep(0.1)
                print ("Stall Current:",SC,"AMPS")
                time.sleep(0.1)
                print ("Free Current:",FC,"AMPS")
                time.sleep(0.1)
                print ("-------------------")

            elif m == '775':
                RPM = 18730
                ST = 0.71
                SC = 134
                FC = 0.7

                print ("-------------------")
                time.sleep(0.1)
                print ("Motor: RS775pro")
                time.sleep(0.1)
                print ("Free Speed:",RPM,"RPM")
                time.sleep(0.1)
                print ("Stall Torque:",ST)
                time.sleep(0.1)
                print ("Stall Current:",SC,"AMPS")
                time.sleep(0.1)
                print ("Free Current:",FC,"AMPS")
                time.sleep(0.1)
                print ("-------------------")

            elif m == 'BAG':
                RPM = 13180
                ST = 0.43
                SC = 53
                FC = 1.8

                print ("-------------------")
                time.sleep(0.1)
                print ("Motor: BAG")
                time.sleep(0.1)
                print ("Free Speed:",RPM,"RPM")
                time.sleep(0.1)
                print ("Stall Torque:",ST)
                time.sleep(0.1)
                print ("Stall Current:",SC,"AMPS")
                time.sleep(0.1)
                print ("Free Current:",FC,"AMPS")
                time.sleep(0.1)
                print ("-------------------")

            p = float(RPM)
            st = float(ST)
            sc = float(SC)
            fc = float(FC)

            CurrentDraw = (((sc-fc)/st*(w*1*cf/gc*4.44822161526*wd*0.0254/2/.90/mc*rT))+fc)
            CD = float(CurrentDraw)
            CDR = round(CD, 2)

            DriveSpeedAdjusted = (p*0.81*((wd*0.0254/2)*2*math.pi)/(0.3048*60)*rT)
            DSA = float(DriveSpeedAdjusted)
            DSAR = round(DSA, 2)

            DriveTrainFreeSpeed = (DSA/0.81)
            DFS = float(DriveTrainFreeSpeed)
            DFSR = round(DFS, 2)

            print ("Overall Ratio:", rOr,":1")
            time.sleep(0.2)
            print ("Drive Train Free Speed:",DFSR,"ft/s")
            time.sleep(0.2)
            print ("Drive Train Adjusted Speed:",DSAR,"ft/s")
            time.sleep(0.2)
            print ("Current Draw Per Motor:",CDR,"AMPS")
            time.sleep(0.2)
            print ("-------------------")

            break

##############################Arm Calculation##################################

        elif DECIDE == 'ARM':
            while True:
                mtr = str(input("Motor Type(CIM/MCIM/775/BAG): "))

                if mtr == 'CIM':
                    break
                elif mtr == 'MCIM':
                    break
                elif mtr == '775':
                    break
                elif mtr == 'BAG':
                    break
                else:
                    print("Invalid Input. Please Try Again.")
                    continue

            m = str(mtr)
            MotorCount = input("Motors Per Gearbox: ")
            mc = float(MotorCount)
            ArmLoad = input("Arm Load: ")
            al = float(ArmLoad)
            ArmLength = input("Arm Length: ")
            ale = float(ArmLength)


            stage = input("Number of Stages: ")
            s = float(stage)

            if s == 1:
                DRIVE1 = input("Driving Gear 1: ")
                DRIVEN1 = input("Driven Gear 1: ")
                DR1 = float(DRIVE1)
                DV1 = float(DRIVEN1)
                DRIVE2 = 1
                DRIVEN2 = 1
                DR2 = float(DRIVE2)
                DV2 = float(DRIVEN2)
                DRIVE3 = 1
                DRIVEN3 = 1
                DR3 = float(DRIVE3)
                DV3 = float(DRIVEN3)
                DRIVE4 = 1
                DRIVEN4 = 1
                DR4 = float(DRIVE4)
                DV4 = float(DRIVEN4)
            elif s == 2:
                DRIVE1 = input("Driving Gear 1: ")
                DRIVEN1 = input("Driven Gear 1: ")
                DR1 = float(DRIVE1)
                DV1 = float(DRIVEN1)
                DRIVE2 = input("Driving Gear 2: ")
                DRIVEN2 = input("Driven Gear 2: ")
                DR2 = float(DRIVE2)
                DV2 = float(DRIVEN2)
                DRIVE3 = 1
                DRIVEN3 = 1
                DR3 = float(DRIVE3)
                DV3 = float(DRIVEN3)
                DRIVE4 = 1
                DRIVEN4 = 1
                DR4 = float(DRIVE4)
                DV4 = float(DRIVEN4)
            elif s == 3:
                DRIVE1 = input("Driving Gear 1: ")
                DRIVEN1 = input("Driven Gear 1: ")
                DR1 = float(DRIVE1)
                DV1 = float(DRIVEN1)
                DRIVE2 = input("Driving Gear 2: ")
                DRIVEN2 = input("Driven Gear 2: ")
                DR2 = float(DRIVE2)
                DV2 = float(DRIVEN2)
                DRIVE3 = input("Driving Gear 3: ")
                DRIVEN3 = input("Driven Gear 3: ")
                DR3 = float(DRIVE3)
                DV3 = float(DRIVEN3)
                DRIVE4 = 1
                DRIVEN4 = 1
                DR4 = float(DRIVE4)
                DV4 = float(DRIVEN4)
            elif s == 4:
                DRIVE1 = input("Driving Gear 1: ")
                DRIVEN1 = input("Driven Gear 1: ")
                DR1 = float(DRIVE1)
                DV1 = float(DRIVEN1)
                DRIVE2 = input("Driving Gear 2: ")
                DRIVEN2 = input("Driven Gear 2: ")
                DR2 = float(DRIVE2)
                DV2 = float(DRIVEN2)
                DRIVE3 = input("Driving Gear 3: ")
                DRIVEN3 = input("Driven Gear 3: ")
                DR3 = float(DRIVE3)
                DV3 = float(DRIVEN3)
                DRIVE4 = input("Driving Gear 4: ")
                DRIVEN4 = input("Driven Gear 4: ")
                DR4 = float(DRIVE4)
                DV4 = float(DRIVEN4)

            r1 = (DV1/DR1)
            r2 = (DV2/DR2)
            r3 = (DV3/DR3)
            r4 = (DV4/DR4)
            rO = (r1*r2*r3*r4)
            rOr = round(rO, 2)
            rT = ((DR1/DV1)*(DR2/DV2)*(DR3/DV3)*(DR4/DV4))

            if m == 'CIM':
                RPM = 5330
                ST = 2.41
                SC = 131
                FC = 2.7

                print ("-------------------")
                time.sleep(0.1)
                print ("Motor: CIM")
                time.sleep(0.1)
                print ("Free Speed:",RPM,"RPM")
                time.sleep(0.1)
                print ("Stall Torque:",ST)
                time.sleep(0.1)
                print ("Stall Current:",SC,"AMPS")
                time.sleep(0.1)
                print ("Free Current:",FC,"AMPS")
                time.sleep(0.1)
                print ("-------------------")

            elif m == 'MCIM':
                RPM = 5840
                ST = 1.41
                SC = 89
                FC = 3

                print ("-------------------")
                time.sleep(0.1)
                print ("Motor: MINI CIM")
                time.sleep()
                print ("Free Speed:",RPM,"RPM")
                time.sleep(0.1)
                print ("Stall Torque:",ST)
                time.sleep(0.1)
                print ("Stall Current:",SC,"AMPS")
                time.sleep(0.1)
                print ("Free Current:",FC,"AMPS")
                time.sleep(0.1)
                print ("-------------------")

            elif m == '775':
                RPM = 18730
                ST = 0.71
                SC = 134
                FC = 0.7

                print ("-------------------")
                time.sleep(0.1)
                print ("Motor: RS775pro")
                time.sleep(0.1)
                print ("Free Speed:",RPM,"RPM")
                time.sleep(0.1)
                print ("Stall Torque:",ST)
                time.sleep(0.1)
                print ("Stall Current:",SC,"AMPS")
                time.sleep(0.1)
                print ("Free Current:",FC,"AMPS")
                time.sleep(0.1)
                print ("-------------------")

            elif m == 'BAG':
                RPM = 13180
                ST = 0.43
                SC = 53
                FC = 1.8

                print ("-------------------")
                time.sleep(0.1)
                print ("Motor: BAG")
                time.sleep(0.1)
                print ("Free Speed:",RPM,"RPM")
                time.sleep(0.1)
                print ("Stall Torque:",ST)
                time.sleep(0.1)
                print ("Stall Current:",SC,"AMPS")
                time.sleep(0.1)
                print ("Free Current:",FC,"AMPS")
                time.sleep(0.1)
                print ("-------------------")

            p = float(RPM)
            st = float(ST)
            sc = float(SC)
            fc = float(FC)

            CurrentDraw = (((((sc*mc)-(fc*mc))/(st*mc))*(al*ale*(rT)/(0.2248*39.37))+(fc*mc))/mc)
            CD = float(CurrentDraw)
            CDR = round(CD, 2)

            StallLoad = (ST*mc*(1/(rT))*39.37*0.2248*0.8/ale)
            STL = float(StallLoad)
            STLR = round(STL, 2)

            SpeedNoLD = (p*rT*(360/60))
            SNL = float(SpeedNoLD)
            SNLR = round(SNL, 2)

            SpeedLD = (((-1)*(SNL/(STL))*(al))+(SNL))
            SL = float(SpeedLD)
            SLR = round(SL, 2)

            NL90 = (90/SNL)
            nl90 = float(NL90)
            nl90r = round(nl90, 2)

            L90 = (90/SL)
            l90 = float(L90)
            l90r = round(l90, 2)



            print ("Overall Ratio:",rOr,":1")
            time.sleep(0.2)
            print ("Stall Load:",STLR,"lbs")
            time.sleep(0.2)
            print ("Arm Rotational Speed Unloaded:",SNLR,"deg/s, 90 deg in",nl90r,"sec")
            time.sleep(0.2)
            print ("Arm Rotational Speed Loaded:",SLR,"deg/s, 90 deg in",l90r,"sec")
            time.sleep(0.2)
            print ("Current Draw Per Motor:",CDR,"AMPS")
            time.sleep(0.2)
            print ("-------------------")

            break

#############################Elevator Calculation##############################

        elif DECIDE == 'ELV':
            while True:
                mtr = str(input("Motor Type(CIM/MCIM/775/BAG): "))

                if mtr == 'CIM':
                    break
                elif mtr == 'MCIM':
                    break
                elif mtr == '775':
                    break
                elif mtr == 'BAG':
                    break
                else:
                    print("Invalid Input. Please Try Again.")
                    continue

            m = str(mtr)
            MotorCount = input("Motors Per Gearbox: ")
            mc = float(MotorCount)
            TravelDistance = input("Travel Distance (in): ")
            tc = float(TravelDistance)
            AppliedLoad = input("Applied Load (lbs): ")
            al = float(AppliedLoad)
            PulleyDia = input("Pulley Diameter (in): ")
            pd = float(PulleyDia)

            stage = input("Number of Stages: ")
            s = float(stage)

            if s == 1:
                DRIVE1 = input("Driving Gear 1: ")
                DRIVEN1 = input("Driven Gear 1: ")
                DR1 = float(DRIVE1)
                DV1 = float(DRIVEN1)
                DRIVE2 = 1
                DRIVEN2 = 1
                DR2 = float(DRIVE2)
                DV2 = float(DRIVEN2)
                DRIVE3 = 1
                DRIVEN3 = 1
                DR3 = float(DRIVE3)
                DV3 = float(DRIVEN3)
                DRIVE4 = 1
                DRIVEN4 = 1
                DR4 = float(DRIVE4)
                DV4 = float(DRIVEN4)
            elif s == 2:
                DRIVE1 = input("Driving Gear 1: ")
                DRIVEN1 = input("Driven Gear 1: ")
                DR1 = float(DRIVE1)
                DV1 = float(DRIVEN1)
                DRIVE2 = input("Driving Gear 2: ")
                DRIVEN2 = input("Driven Gear 2: ")
                DR2 = float(DRIVE2)
                DV2 = float(DRIVEN2)
                DRIVE3 = 1
                DRIVEN3 = 1
                DR3 = float(DRIVE3)
                DV3 = float(DRIVEN3)
                DRIVE4 = 1
                DRIVEN4 = 1
                DR4 = float(DRIVE4)
                DV4 = float(DRIVEN4)
            elif s == 3:
                DRIVE1 = input("Driving Gear 1: ")
                DRIVEN1 = input("Driven Gear 1: ")
                DR1 = float(DRIVE1)
                DV1 = float(DRIVEN1)
                DRIVE2 = input("Driving Gear 2: ")
                DRIVEN2 = input("Driven Gear 2: ")
                DR2 = float(DRIVE2)
                DV2 = float(DRIVEN2)
                DRIVE3 = input("Driving Gear 3: ")
                DRIVEN3 = input("Driven Gear 3: ")
                DR3 = float(DRIVE3)
                DV3 = float(DRIVEN3)
                DRIVE4 = 1
                DRIVEN4 = 1
                DR4 = float(DRIVE4)
                DV4 = float(DRIVEN4)
            elif s == 4:
                DRIVE1 = input("Driving Gear 1: ")
                DRIVEN1 = input("Driven Gear 1: ")
                DR1 = float(DRIVE1)
                DV1 = float(DRIVEN1)
                DRIVE2 = input("Driving Gear 2: ")
                DRIVEN2 = input("Driven Gear 2: ")
                DR2 = float(DRIVE2)
                DV2 = float(DRIVEN2)
                DRIVE3 = input("Driving Gear 3: ")
                DRIVEN3 = input("Driven Gear 3: ")
                DR3 = float(DRIVE3)
                DV3 = float(DRIVEN3)
                DRIVE4 = input("Driving Gear 4: ")
                DRIVEN4 = input("Driven Gear 4: ")
                DR4 = float(DRIVE4)
                DV4 = float(DRIVEN4)

            r1 = (DV1/DR1)
            r2 = (DV2/DR2)
            r3 = (DV3/DR3)
            r4 = (DV4/DR4)
            rO = (r1*r2*r3*r4)
            rOr = round(rO, 2)
            rT = ((DR1/DV1)*(DR2/DV2)*(DR3/DV3)*(DR4/DV4))

            if m == 'CIM':
                RPM = 5330
                ST = 2.41
                SC = 131
                FC = 2.7

                print ("-------------------")
                time.sleep(0.1)
                print ("Motor: CIM")
                time.sleep(0.1)
                print ("Free Speed:",RPM,"RPM")
                time.sleep(0.1)
                print ("Stall Torque:",ST)
                time.sleep(0.1)
                print ("Stall Current:",SC,"AMPS")
                time.sleep(0.1)
                print ("Free Current:",FC,"AMPS")
                time.sleep(0.1)
                print ("-------------------")

            elif m == 'MCIM':
                RPM = 5840
                ST = 1.41
                SC = 89
                FC = 3

                print ("-------------------")
                time.sleep(0.1)
                print ("Motor: MINI CIM")
                time.sleep()
                print ("Free Speed:",RPM,"RPM")
                time.sleep(0.1)
                print ("Stall Torque:",ST)
                time.sleep(0.1)
                print ("Stall Current:",SC,"AMPS")
                time.sleep(0.1)
                print ("Free Current:",FC,"AMPS")
                time.sleep(0.1)
                print ("-------------------")

            elif m == '775':
                RPM = 18730
                ST = 0.71
                SC = 134
                FC = 0.7

                print ("-------------------")
                time.sleep(0.1)
                print ("Motor: RS775pro")
                time.sleep(0.1)
                print ("Free Speed:",RPM,"RPM")
                time.sleep(0.1)
                print ("Stall Torque:",ST)
                time.sleep(0.1)
                print ("Stall Current:",SC,"AMPS")
                time.sleep(0.1)
                print ("Free Current:",FC,"AMPS")
                time.sleep(0.1)
                print ("-------------------")

            elif m == 'BAG':
                RPM = 13180
                ST = 0.43
                SC = 53
                FC = 1.8

                print ("-------------------")
                time.sleep(0.1)
                print ("Motor: BAG")
                time.sleep(0.1)
                print ("Free Speed:",RPM,"RPM")
                time.sleep(0.1)
                print ("Stall Torque:",ST)
                time.sleep(0.1)
                print ("Stall Current:",SC,"AMPS")
                time.sleep(0.1)
                print ("Free Current:",FC,"AMPS")
                time.sleep(0.1)
                print ("-------------------")

            p = float(RPM)
            st = float(ST)
            sc = float(SC)
            fc = float(FC)

            CurrentDraw = (((((sc*mc)-(fc*mc))/(st*mc))*(al*pd/2*(rT)/(0.2248*39.37))+(fc*mc))/mc)
            CD = float(CurrentDraw)
            CDR = round(CD, 2)

            StallLoad = (st*mc*(1/(rT))*39.37*0.2248*0.80/(pd/2))
            stl = float(StallLoad)
            STLR = round(stl, 2)

            LinearSpeedNoLoad = ((p*(rT)*(360/60))*math.pi*2*(pd/2)/360)
            LSNL = float(LinearSpeedNoLoad)
            LSNLR = round(LSNL, 2)

            LinearSpeedLoad = ((((-1)*((p*(rT)*(360/60))/(stl))*(al))+(p*(rT)*(360/60)))*(math.pi*2*(pd/2)/360))
            LSL = float(LinearSpeedLoad)
            LSLR = round(LSL, 2)

            print ("Overall Ratio:",rOr,":1")
            time.sleep(0.2)
            print ("Stall Load:",STLR,"lbs")
            time.sleep(0.2)
            print ("Elevator Linear Speed Unloaded:",LSNLR,"in/s")
            time.sleep(0.2)
            print ("Elevator Linear Speed Loaded:",LSLR, "in/s")
            time.sleep(0.2)
            print ("Current Draw Per Motor:",CDR,"AMPS")
            time.sleep(0.2)
            print ("-------------------")

            break

#############################Intake Calculation################################

        elif DECIDE == 'INT':
            while True:
                mtr = str(input("Motor Type(CIM/MCIM/775/BAG): "))

                if mtr == 'CIM':
                    break
                elif mtr == 'MCIM':
                    break
                elif mtr == '775':
                    break
                elif mtr == 'BAG':
                    break
                else:
                    print("Invalid Input. Please Try Again.")
                    continue

            m = str(mtr)
            MotorCount = input("Motors Per Gearbox: ")
            mc = float(MotorCount)
            TravelDistance = input("Travel Distance(in): ")
            td = float(TravelDistance)
            IntakeSideNum = input("Number of Intake Sides: ")
            isn = float(IntakeSideNum)
            RollerDiameter = input("Roller Diameter(in): ")
            rd = float(RollerDiameter)
            DragLoad = input("Drag Load(lbs): ")
            dl = float(DragLoad)

            stage = input("Number of Stages: ")
            s = float(stage)

            if s == 1:
                DRIVE1 = input("Driving Gear 1: ")
                DRIVEN1 = input("Driven Gear 1: ")
                DR1 = float(DRIVE1)
                DV1 = float(DRIVEN1)
                DRIVE2 = 1
                DRIVEN2 = 1
                DR2 = float(DRIVE2)
                DV2 = float(DRIVEN2)
                DRIVE3 = 1
                DRIVEN3 = 1
                DR3 = float(DRIVE3)
                DV3 = float(DRIVEN3)
                DRIVE4 = 1
                DRIVEN4 = 1
                DR4 = float(DRIVE4)
                DV4 = float(DRIVEN4)
            elif s == 2:
                DRIVE1 = input("Driving Gear 1: ")
                DRIVEN1 = input("Driven Gear 1: ")
                DR1 = float(DRIVE1)
                DV1 = float(DRIVEN1)
                DRIVE2 = input("Driving Gear 2: ")
                DRIVEN2 = input("Driven Gear 2: ")
                DR2 = float(DRIVE2)
                DV2 = float(DRIVEN2)
                DRIVE3 = 1
                DRIVEN3 = 1
                DR3 = float(DRIVE3)
                DV3 = float(DRIVEN3)
                DRIVE4 = 1
                DRIVEN4 = 1
                DR4 = float(DRIVE4)
                DV4 = float(DRIVEN4)
            elif s == 3:
                DRIVE1 = input("Driving Gear 1: ")
                DRIVEN1 = input("Driven Gear 1: ")
                DR1 = float(DRIVE1)
                DV1 = float(DRIVEN1)
                DRIVE2 = input("Driving Gear 2: ")
                DRIVEN2 = input("Driven Gear 2: ")
                DR2 = float(DRIVE2)
                DV2 = float(DRIVEN2)
                DRIVE3 = input("Driving Gear 3: ")
                DRIVEN3 = input("Driven Gear 3: ")
                DR3 = float(DRIVE3)
                DV3 = float(DRIVEN3)
                DRIVE4 = 1
                DRIVEN4 = 1
                DR4 = float(DRIVE4)
                DV4 = float(DRIVEN4)
            elif s == 4:
                DRIVE1 = input("Driving Gear 1: ")
                DRIVEN1 = input("Driven Gear 1: ")
                DR1 = float(DRIVE1)
                DV1 = float(DRIVEN1)
                DRIVE2 = input("Driving Gear 2: ")
                DRIVEN2 = input("Driven Gear 2: ")
                DR2 = float(DRIVE2)
                DV2 = float(DRIVEN2)
                DRIVE3 = input("Driving Gear 3: ")
                DRIVEN3 = input("Driven Gear 3: ")
                DR3 = float(DRIVE3)
                DV3 = float(DRIVEN3)
                DRIVE4 = input("Driving Gear 4: ")
                DRIVEN4 = input("Driven Gear 4: ")
                DR4 = float(DRIVE4)
                DV4 = float(DRIVEN4)

            r1 = (DV1/DR1)
            r2 = (DV2/DR2)
            r3 = (DV3/DR3)
            r4 = (DV4/DR4)
            rO = (r1*r2*r3*r4)
            rOr = round(rO, 2)
            rT = ((DR1/DV1)*(DR2/DV2)*(DR3/DV3)*(DR4/DV4))

            if m == 'CIM':
                RPM = 5330
                ST = 2.41
                SC = 131
                FC = 2.7

                print ("-------------------")
                time.sleep(0.1)
                print ("Motor: CIM")
                time.sleep(0.1)
                print ("Free Speed:",RPM,"RPM")
                time.sleep(0.1)
                print ("Stall Torque:",ST)
                time.sleep(0.1)
                print ("Stall Current:",SC,"AMPS")
                time.sleep(0.1)
                print ("Free Current:",FC,"AMPS")
                time.sleep(0.1)
                print ("-------------------")

            elif m == 'MCIM':
                RPM = 5840
                ST = 1.41
                SC = 89
                FC = 3

                print ("-------------------")
                time.sleep(0.1)
                print ("Motor: MINI CIM")
                time.sleep()
                print ("Free Speed:",RPM,"RPM")
                time.sleep(0.1)
                print ("Stall Torque:",ST)
                time.sleep(0.1)
                print ("Stall Current:",SC,"AMPS")
                time.sleep(0.1)
                print ("Free Current:",FC,"AMPS")
                time.sleep(0.1)
                print ("-------------------")

            elif m == '775':
                RPM = 18730
                ST = 0.71
                SC = 134
                FC = 0.7

                print ("-------------------")
                time.sleep(0.1)
                print ("Motor: RS775pro")
                time.sleep(0.1)
                print ("Free Speed:",RPM,"RPM")
                time.sleep(0.1)
                print ("Stall Torque:",ST)
                time.sleep(0.1)
                print ("Stall Current:",SC,"AMPS")
                time.sleep(0.1)
                print ("Free Current:",FC,"AMPS")
                time.sleep(0.1)
                print ("-------------------")

            elif m == 'BAG':
                RPM = 13180
                ST = 0.43
                SC = 53
                FC = 1.8

                print ("-------------------")
                time.sleep(0.1)
                print ("Motor: BAG")
                time.sleep(0.1)
                print ("Free Speed:",RPM,"RPM")
                time.sleep(0.1)
                print ("Stall Torque:",ST)
                time.sleep(0.1)
                print ("Stall Current:",SC,"AMPS")
                time.sleep(0.1)
                print ("Free Current:",FC,"AMPS")
                time.sleep(0.1)
                print ("-------------------")

            p = float(RPM)
            st = float(ST)
            sc = float(SC)
            fc = float(FC)

            CurrentDraw = ((((sc*mc)-(fc*mc))/(st*mc))*(dl/2*(rT)*fc/(0.2248*39.37)+(fc*mc))/mc)
            CD = float(CurrentDraw)
            CDR = round(CD, 2)

            StallDragLoad = (st*mc*(1/(rT))*39.37*0.2248*0.80/(rd/2))
            SDL = float(StallDragLoad)
            SDLR = round(SDL, 2)

            IntakeLSpeedNoLoad = ((p*(rT)*(360/60))*math.pi*2*(rd/2)/360*isn)
            ILSNL = float(IntakeLSpeedNoLoad)
            ILSNLR = round(ILSNL, 2)

            IntakeSpeedLoad = ((((-1)*((p*(rT)*(360/60))/(StallDragLoad))*(dl))+(p*(rT)*(360/60)))*(math.pi*2(rd/2)/360)*IntakeSideNum)
            ILSL = float(IntakeSpeedLoad)
            ILSLR = round(ILSL, 2)

            print ("Overall Ratio:",rOr,":1")
            time.sleep(0.2)
            print ("Stall Drag Load:",SDLR,"lbs")
            time.sleep(0.2)
            print ("Intake Linear Speed Unloaded:",ILSNLR,"in/s")
            time.sleep(0.2)
            print ("Intake Linear Speed Loaded:",ILSLR, "in/s")
            time.sleep(0.2)
            print ("Current Draw Per Motor:",CDR,"AMPS")
            time.sleep(0.2)
            print ("-------------------")

            break

###############################################################################
        else:
            print("Invalid Input. Please Try Again.")
            continue
###############################################################################
    ANS = str(input("Would you like to do something else? Y/N "))
    if ANS == 'N':
        break
    elif ANS == 'Y':
        continue
