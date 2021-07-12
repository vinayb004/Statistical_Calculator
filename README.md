[![Build Status](https://travis-ci.com/vinayb004/Statistical_Calculator.svg?branch=master)](https://travis-ci.com/vinayb004/Statistical_Calculator)

# Statistical-calculator

## Task list
No. |Task | Short Description
------- | --------------- | ---------- | 
1| Class Diagram | An outline showing how each of the statistical and calculator functions relates to each other
2| Connect Travis-CI with Github repo | Configure automation testing on all branches using Travis 
3| Project management board | Development task breakdown to the function level 
4| Baseline the Basic Calculator functions | Addition, Subtraction, Division, Multiplication, Square, Square Root 
5| Descriptive Statistics functions | Functions- mean, median, mode, standard Deviation 
6| Random Generator | Generate a random number without a seed between a range of two numbers, Generate a random number with a seed between a range of two numbers, Generate a list of N random numbers with a seed and between a range of numbers, Select a random item from a list, Set a seed and randomly. select the same value from a list, Select N number of items from a list without a seed, Select N number of items from a list with a seed 
7| Readme | Task breakdown, description, formulas and result 

## Function list
No. | Function | Short Description  Formula | Example | Result 
------- | --------------- | ---------- | ----------- | ----------- | 
1 | Addition | a + b | 12+3 | 15
2 | Subtraction| b-a | 13-2 | 11
3 | Multiplication| a * b |5 * 2 | 10
4 | Division | b/a | 12/4 | 3
5 | Square | a * a | 5 * 5 | 25
6 | Sqaure Root | math.sqrt(a)| math.sqrt(635)| 25.19920633
7 | Mean | sum(data)/len(data)| 15/3 |data=[1,2,3,4,5] Result = 3
8 | Median |  ((n + 1)/2)th (even number of elements) (((n+1)/2) -1)(odd number of elements), n is len(data)| (5+1)/2 |odd:data=[1,2,3,4,5] Result = 3,even:[1,2,3,4,5,6] Result = 3.5 
9 | Mode | max(frequency) Mode is calculated by counting the frequencies of an element in a list and calculating the max of all frequencies. | max(2,3,1,1,1,1,1) |data=[1,2,5,1,2,3,6,2,9,10,2] Result = 2(count 3)
10 | Variance | s=((sum(x-x")* * 2/len(data-1))|((sum(data[i]-mean(data))* * 2/len(data)-1)| data=[1,2,3,4,5] Result = 2
11 | Standard deviation | sqrt(variance) | sqrt(2) | data=[1,2,3,4,5] Result = 1.414


## Class Diagram of Statistics, Calculator and related classes 
<object data="Diagram_Vinay.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="Diagram_Vinay.pdf">
        <p>Click here to veiw/download the class diagram in PDF format: <a href="Diagram_Vinay.pdf">Class Diagram</a>.</p>
    </embed>
</object>
