<cfparam name="urlToFetch" default="https://google.com/">
<!--- Step 1: Fetch HTML from the website --->

<cfhttp url="#urlToFetch#" method="get" result="httpResponse" throwonerror="yes"></cfhttp>

<!--- Step 2: Save HTML to temp file --->
<cfset htmlFilePath = expandPath("temp_fetched.html")>
<cffile action="write" file="#htmlFilePath#" output="#httpResponse.fileContent#" charset="utf-8">

<!--- Step 3: Set Python path and script path --->
<cfset pythonExe = "C:\Users\DELL\AppData\Local\Programs\Python\Python313\python.exe">
<cfset scriptFile = expandPath("extract_keywords_spacy.py")>
<cfset keywordOutput = "">
<cfset errorOutput = "">

<!--- Step 4: Run the Python script using cfexecute --->
<cfexecute name="#pythonExe#"
    arguments="#scriptFile# ""#htmlFilePath#"""
    variable="keywordOutput"
    errorVariable="errorOutput"
    timeout="30">
</cfexecute>

<!--- Step 5: Output results --->
<cfoutput>
    <h3>Extracted Keywords for Meta Tags from <code>#urlToFetch#</code>:</h3>
    <cfif len(trim(errorOutput))>
        <p style="color: red;"><strong>Error:</strong> #htmlEditFormat(errorOutput)#</p>
    <cfelse>
        <meta name="keywords" content="#htmlEditFormat(trim(keywordOutput))#">
        <ul>
            <cfloop list="#keywordOutput#" index="word" delimiters=",">
                <li>#trim(word)#</li>
            </cfloop>
        </ul>
    </cfif>
</cfoutput>

