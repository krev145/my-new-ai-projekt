# **AI-powered Speed and Compound Interest Calculator**  
Final project for the Building AI course  

## **Summary**  
This project aims to develop an AI-driven calculator for speed conversions and compound interest calculations. The calculator will allow users to effortlessly convert between **minutes per kilometer (min/km) and kilometers per hour (km/h)** while also providing a **compound interest simulator** with adjustable parameters for investment years, monthly contributions, and interest rates.  

---

## **Background**  
Many runners, cyclists, and fitness enthusiasts frequently switch between different speed units, but manual conversions can be tedious. Similarly, financial planning is crucial for long-term wealth building, but many people find it difficult to grasp the **power of compound interest** and how small contributions grow over time.  

**Problems solved:**  
- Difficulty in converting between **min/km and km/h** efficiently.  
- Lack of an **intuitive, adjustable compound interest calculator** for financial planning.  
- Need for an AI-assisted tool that provides **smart insights based on user inputs**.  

**Personal motivation:**  
I have a strong interest in both **sports performance** and **financial literacy**. By combining AI with computational models, this project will provide an easy-to-use tool for both **athletes** and **investors** to optimize their training and savings strategies.  

---

## **How is it used?**  
The solution will consist of **two main features**:  

### **1️⃣ Speed Converter**  
A user can input either:  
✅ **Minutes per kilometer (min/km)** → Converts to **kilometers per hour (km/h)**.  
✅ **Kilometers per hour (km/h)** → Converts to **minutes per kilometer (min/km)**.  
✅ AI-based suggestions for **target paces** based on previous inputs.  

### **2️⃣ Compound Interest Calculator**  
Users can adjust:  
✅ **Investment period (years)**  
✅ **Monthly contributions**  
✅ **Expected interest rate**  
✅ **Compounding frequency (monthly, yearly, etc.)**  

The tool will visualize the **growth of investments over time**, highlighting the impact of compound interest.  

**Target users:**  
- **Runners, cyclists, and fitness enthusiasts** who want to analyze and optimize their speed data.  
- **Investors and savers** who want to understand the power of compound interest.  
- **Coaches and financial advisors** who need an interactive tool for training and financial planning.  

---

## **Data Sources and AI Methods**  
### **Speed Conversion Model:**  
- **Mathematical formulas** for unit conversion:  
  \[
  \text{Speed (km/h)} = \frac{60}{\text{Pace (min/km)}}
  \]
  \[
  \text{Pace (min/km)} = \frac{60}{\text{Speed (km/h)}}
  \]

- **AI-enhanced training pace recommendations** using:  
  - **Regression models** to predict optimal training paces based on previous performances.  
  - **Machine learning algorithms** for customized pace suggestions based on fitness level.  

### **Compound Interest Model:**  
- **Standard compound interest formula**:  
  \[
  A = P \times (1 + \frac{r}{n})^{n \times t}
  \]
  where:  
  - \( A \) = Final amount  
  - \( P \) = Monthly contribution  
  - \( r \) = Annual interest rate  
  - \( n \) = Compounding frequency  
  - \( t \) = Number of years  

- **Simulation and visualization** using:  
  - **AI-powered trend analysis** to suggest different saving strategies.  
  - **Graphical representation** of investment growth over time.  

---

## **Challenges**  
- **Real-world variations in running speeds:** Different terrains and conditions affect pace.  
- **Unpredictable financial markets:** Interest rates fluctuate, affecting long-term predictions.  
- **User education:** Many people struggle to understand **financial principles** and **pace calculations**.  

---

## **What next?**  
- **Develop a web or mobile app** for easy accessibility.  
- **Include currency inflation adjustments** for realistic future value calculations.  
- **Expand AI training recommendations** with real user data to suggest race paces.  
- **Integrate real-time financial data** (e.g., historical interest rates, inflation).  

To expand this project, **collaborations with coaches, financial experts, and data scientists** would be valuable.  

---

## **Acknowledgments**  
- Speed conversion formulas are based on **standard running pace calculations**.  
- Compound interest calculations follow **standard financial principles**.  
- Uses **open-source AI libraries** (NumPy, SciPy, TensorFlow, Scikit-learn) for data modeling.  

---

🚀 **This AI-powered tool will help both athletes and investors make data-driven decisions effortlessly!** 🏃‍♂️💰



-------------------------------------------------------------------------------------------------------
# my-new-ai-projekt
Building AI course projekt


Background: What is the problem your idea will solve? How common or frequent is this problem? What is your personal motivation? Why is this topic important or interesting?
Data and AI techniques: What data sources does your project depend on? Almost all AI solutions depend on some data. The availability and quality of the data are essential. Which AI techniques do you think will be helpful? Depending on whether you've been doing the programming exercises or not, you may choose to include a concrete demo implemented by coding, using some actual data!
How is it used: What is the context in which your solution is used, and by whom? Who are the people affected by it? It’s important to appreciate the viewpoints of all those affected.
Challenges: What does your project not solve? It’s important to understand that any technological solution will have its limitations.
What next: How could your project grow and become something even more?
Acknowledgments: If you’re using open source code or documents in your project, make sure you give credit to the creators. Mention your sources of inspiration, too.
<!-- This is the markdown template for the final project of the Building AI course, 
created by Reaktor Innovations and University of Helsinki. 
Copy the template, paste it to your GitHub README and edit! -->

# Project Title

Final project for the Building AI course

## Summary

Describe briefly in 2-3 sentences what your project is about. About 250 characters is a nice length! 


## Background

Which problems does your idea solve? How common or frequent is this problem? What is your personal motivation? Why is this topic important or interesting?

This is how you make a list, if you need one:
* problem 1
* problem 2
* etc.


## How is it used?

Describe the process of using the solution. In what kind situations is the solution needed (environment, time, etc.)? Who are the users, what kinds of needs should be taken into account?

Images will make your README look nice!
Once you upload an image to your repository, you can link link to it like this (replace the URL with file path, if you've uploaded an image to Github.)
![Cat](https://upload.wikimedia.org/wikipedia/commons/5/5e/Sleeping_cat_on_her_back.jpg)

If you need to resize images, you have to use an HTML tag, like this:
<img src="https://upload.wikimedia.org/wikipedia/commons/5/5e/Sleeping_cat_on_her_back.jpg" width="300">

This is how you create code examples:
```
def main():
   countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
   pop = [5615000, 5439000, 324000, 5080000, 9609000]   # not actually needed in this exercise...
   fishers = [1891, 2652, 3800, 11611, 1757]

   totPop = sum(pop)
   totFish = sum(fishers)

   # write your solution here

   for i in range(len(countries)):
      print("%s %.2f%%" % (countries[i], 100.0))    # current just prints 100%

main()
```


## Data sources and AI methods
Where does your data come from? Do you collect it yourself or do you use data collected by someone else?
If you need to use links, here's an example:
[Twitter API](https://developer.twitter.com/en/docs)

| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |

## Challenges

What does your project _not_ solve? Which limitations and ethical considerations should be taken into account when deploying a solution like this?

## What next?

How could your project grow and become something even more? What kind of skills, what kind of assistance would you  need to move on? 


## Acknowledgments

* list here the sources of inspiration 
* do not use code, images, data etc. from others without permission
* when you have permission to use other people's materials, always mention the original creator and the open source / Creative Commons licence they've used
  <br>For example: [Sleeping Cat on Her Back by Umberto Salvagnin](https://commons.wikimedia.org/wiki/File:Sleeping_cat_on_her_back.jpg#filelinks) / [CC BY 2.0](https://creativecommons.org/licenses/by/2.0)
* etc
