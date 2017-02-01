import java.io.File;
import java.io.FilenameFilter;
import java.io.IOException;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;

public class InputFileReader {
	private Document docs[];
	private String filePaths[];
	private GenericExtFilter filter;

	public InputFileReader(String fileExtension) {
		filter = new GenericExtFilter(fileExtension);
	}

	public void loadFromFile() throws IOException {
		// Quelle http://jsoup.org/cookbook/input/load-document-from-file

		String target_dir = "./stringdata";
		File dir = new File(target_dir);
		File[] files = dir.listFiles(filter);
		docs = new Document[files.length];
		filePaths = new String[files.length];
		for (int i = 0; i < files.length; i++) {
			System.out.println(files[i].getPath()
					+ " als HTML eingelesen.");
			filePaths[i] = files[i].getPath();
			docs[i] = Jsoup.parse(files[i], "UTF-8", "");
			//http://stackoverflow.com/questions/7703434/jsoup-character-encoding-issue
			//docs[i] = Jsoup.parse(files[i], "ISO-8859-1", "");
		}

	}

	public int anzahlDokumente() {
		return docs.length;
	}

	public Document dokumentAusgabe(int index) {
		return docs[index];
	}

	public String dateiPfadAusgabe(int index) {
		return filePaths[index];
	}

	public class GenericExtFilter implements FilenameFilter {

		private String ext;

		public GenericExtFilter(String ext) {
			this.ext = ext;
		}

		public boolean accept(File dir, String name) {
			return (name.contains(ext));
		}
	}

}
