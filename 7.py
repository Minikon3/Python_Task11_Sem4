import re

#r"begin loc list\((.*?)\)?\s*=:?\s*@'(.*?)'\. end"
def parse_string(input_string):
    matches = re.findall(
        r"begin\s*loc\s*list\((.*?)\)?\s*=:?\s*@'(.*?)'\. end",
        input_string, re.DOTALL)
    result = []
    for match in matches:
        data = match[0].split()
        result.append((match[1], data))
    return result

print(parse_string("begin loc list( usbi zaza_798 ) =: @'usan'. end begin loc list( laed\nbereadi_959 ) =:@'xeteed'. end begin loc list( atra_877 orzate_982\nonon_895 ) =: @'soma_465'. end begin loc list( enated_902 raqure_487\norrice ) =: @'inlaor'. end"))

print('\n')

input_string = "begin loc list( bira istidi_408 ) =: @'arre'. end begin loc list(\nerra_452 atza qued )=: @'mabige'. end begin loc list(atxeon_354\nberi_601 ) =:@'bear'. end"
parsed_data = parse_string(input_string)
print(parsed_data)

print('\n')

input_string = "begin loc list( gezaan_476 zaen mareri ritece_201)=: @'atti_341'. end\nbegin loc list( cean_443 ceanle_602 gean_51 ) =: @'vequ'. end begin\nloc list( bea aenri tirain_758) =:@'andidi_237'. end"
parsed_data = parse_string(input_string)
print(parsed_data)

print('\n')

input_string = "begin loc list(sorile_69 quis orqu_258 erso ) =: @'tira_315'. end\nbegin loc list(arrais quan )=:@'leaso'. end begin loc list(tege\nedorce_147 arteis_663 veandi_920 ) =: @'gebete'. end begin loc\nlist(veanis_773 xea_578 zadi_747) =:@'ceso_192'. end"
parsed_data = parse_string(input_string)
print(parsed_data)
