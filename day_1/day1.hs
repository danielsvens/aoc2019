-- part 1

readInt::String -> Int
readInt = read

calcFuel::Int -> Int
calcFuel mass = mass `div` 3 - 2

main = do
    massList <- readFile "input.txt"
    print . sum . map calcFuel . map readInt . words $ massList
