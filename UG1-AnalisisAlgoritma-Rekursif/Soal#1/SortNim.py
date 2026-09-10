def InsertRecursive(sorted_array, current_value, current_length, is_odd):
    # TODO 1: Implementasikan base case, logika komparasi pengurutan sesuai NIM, 
    # dan pemanggilan rekursi fungsi insert.
    
    if current_length == 0:
        return [current_value]

    last = sorted_array[current_length - 1]

    if is_odd:
        if current_value >= last:
            return sorted_array[:current_length] + [current_value]
        else:
            return InsertRecursive(sorted_array[:current_length-1], current_value, current_length-1, is_odd) + [last]
    else:
        if current_value <= last:
            return sorted_array[:current_length] + [current_value]
        else:
            return InsertRecursive(sorted_array[:current_length-1], current_value, current_length-1, is_odd) + [last]


def RecursiveFilterSort(data_array, current_length, is_odd):
    # TODO 2: Implementasikan base case, pemecahan rekursif, dan filter kondisional 
    # untuk memanggil fungsi InsertRecursive sesuai paritas NIM.
     # Base case
    if current_length == 0:
        return []


    current_value = data_array[current_length - 1]

    # Rekursi untuk sisa array
    result = RecursiveFilterSort(data_array, current_length - 1, is_odd)

    # Filter sesuai aturan NIM
    if is_odd and current_value % 2 == 1:
        return InsertRecursive(result, current_value, len(result), is_odd)
    elif not is_odd and current_value % 2 == 0:
        return InsertRecursive(result, current_value, len(result), is_odd)
    else:
        return result


NIM_MAHASISWA = "71251186"

if NIM_MAHASISWA != "":
    raw_data = [int(digit) for digit in NIM_MAHASISWA]
    data_length = len(raw_data)
    
    is_odd = int(NIM_MAHASISWA[-1]) % 2 == 1
    tipe = "GANJIL (Ascending)" if is_odd else "GENAP (Descending)"
    
    final_result = RecursiveFilterSort(raw_data, data_length, is_odd)

    # TODO 
    print("===== FILTER & SORT NIM =====")
    print("NIM Mahasiswa  :", NIM_MAHASISWA)
    print("Tipe           :", tipe)
    print("Data Digit Awal:", raw_data)
    print("Hasil Akhir    :", final_result)