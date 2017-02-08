import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.safety.Whitelist;

public class DataSearcher {

		// Dokument roh
		private Document doc;

		// Extraktion Metadaten
		private String filePath;
		
		Songs corpus;

		public DataSearcher() {
			corpus = new Songs();
		}

		public void setDocumentToReadFrom(Document doc, String filePath) {
			this.doc = doc;
			this.filePath = filePath;
		}

		public void extractData() {
			generateSongList(doc);

		}
		
		private String extractDate(String input){
			String output = "";
			Matcher match = findeTextausschnitte("\\((\\d{4})\\)", input);
			if (match.find()){
				//output = input.substring(match.end(), input.length()-1);
				output = match.group(1);
				output = output.substring(0, 4);
				//System.out.println(dokText);
			}
			
			return output;
		}
		
		private String cleanAlbum(String input){
			String output = "";
			output = input.replaceAll("\\((.*)\\)", "");
			output = output.substring(0, output.length()-1);
			
			return output;
		}
		
		// Findet alle Redner, deren Reden von einem Ereignis unterbrochen werden
		private void generateSongList(Document doc) {
			
			String title = "title";
			String text = "text";
			String date = "date";
			String album = "album";
			String author = "author"; 
			
			title = cleanText(doc.getElementsByAttributeValue("id", "song-header-title").toString());
			text = cleanText(doc.getElementsByAttributeValue("class", "lyricbox").toString());
			date = extractDate(cleanText(doc.getElementsByAttributeValue("id", "song-header-container").toString()));
			try{
				album = cleanAlbum(cleanText(doc.getElementsByAttributeValue("id", "song-header-container").get(0).getElementsByTag("i").toString()));
			}catch(IndexOutOfBoundsException e){
				System.out.println(e.toString());
				album = "unknown";
			}
				// some files don't credit an author, thats why a try/catch block is needed
			try{	
				author = cleanText(doc.getElementsByAttributeValue("class", "song-credit-box").get(0).child(0).child(0).child(1).toString());
			}catch(IndexOutOfBoundsException e){
				System.out.println(e.toString());
				author = "unknown";
			}
			// System.out.println("Der Author: " + author );
			
			corpus.newSong(title, text, date, album, author, filePath);
		}
		
		//TODO
		public String cleanText(String uncleanText){
			String cleanText = "";
			
			cleanText = Jsoup.clean(uncleanText, "", Whitelist.none(), new Document.OutputSettings().prettyPrint(false))
					.replaceAll("&lt;br&gt;", "")
					.replaceAll("\\"+Character.toString('\u00AD'), "")
					.replaceAll("(<|>)", "")
					.replaceAll("\\*", "")
					.replaceAll("&amp;", "");
			

			return cleanText;
		}

		
		public int getNumberOfSongs(){
			return corpus.getNumberOfSongs();
		}

		
		public int getId(int index) {
			try {
				return corpus.getId(index);
			} catch (IndexOutOfBoundsException e) {
				if (Configurations.showExceptions) {
					e.printStackTrace();
				}
				return 0;
			}
		}

		public String getTitle(int index) {
			try {
				return corpus.getTitle(index);
			} catch (IndexOutOfBoundsException e) {
				if (Configurations.showExceptions) {
					e.printStackTrace();
				}
				return "";
			}
		}
		
		public String getText(int index) {
			try {
				return corpus.getText(index);
			} catch (IndexOutOfBoundsException e) {
				if (Configurations.showExceptions) {
					e.printStackTrace();
				}
				return "";
			}
		}
		
		public String getDate(int index) {
			try {
				return corpus.getDate(index);
			} catch (IndexOutOfBoundsException e) {
				if (Configurations.showExceptions) {
					e.printStackTrace();
				}
				return "";
			}
		}
		public String getAlbum(int index) {
			try {
				return corpus.getAlbum(index);
			} catch (IndexOutOfBoundsException e) {
				if (Configurations.showExceptions) {
					e.printStackTrace();
				}
				return "";
			}
		}
		public String getAuthor(int index) {
			try {
				return corpus.getAuthor(index);
			} catch (IndexOutOfBoundsException e) {
				if (Configurations.showExceptions) {
					e.printStackTrace();
				}
				return "";
			}
		}
		
		public String getFilePath(int index){
			return corpus.getFilePath(index);
		}

		private Matcher findeTextausschnitte(String regex, String textdatenRoh) {
			Pattern pattern = Pattern.compile(regex);
			Matcher matcher = pattern.matcher(textdatenRoh);
			return matcher;
		}
		
}
