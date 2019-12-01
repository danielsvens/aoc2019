readInt::String -> Int
readInt = read

calcFuel::Int -> Int
calcFuel mass = mass `div` 3 - 2

calcFuelRec::Int -> Int
calcFuelRec mass
    | mass < 0 = 0
    | otherwise = mass + calcFuelRec (calcFuel mass)

main = do
    massList <- readFile "input.txt"

    -- part 1
    print . sum . map calcFuel . map readInt . words $ massList
    
    -- part 2
    print(sum([calcFuelRec y - y | y <- map readInt . words $ massList]))
