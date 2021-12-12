package edu.stanford.cs246.wordcount;

import java.io.IOException;
import java.util.Arrays;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.input.TextInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

public class WordCount extends Configured implements Tool {
    public static void main(String[] args) throws Exception {
        System.out.println(Arrays.toString(args));
        int result = ToolRunner.run(new Configuration(), new WordCount(), args);
        
        System.exit(result);
    }
    
    @Override
    public int run(String[] args) throws Exception 
    {
        System.out.println(Arrays.toString(args));
        Job job1 = new Job(getConf(), "WordCount");
        job1.setJarByClass(WordCount.class);
        job1.setOutputKeyClass(Text.class);
        job1.setOutputValueClass(IntWritable.class);
        
        job1.setMapperClass(Map1.class);
        job1.setReducerClass(Reduce1.class);
        
        job1.setInputFormatClass(TextInputFormat.class);
        job1.setOutputFormatClass(TextOutputFormat.class);
        
        FileInputFormat.addInputPath(job1, new Path(args[0]));
        FileOutputFormat.setOutputPath(job1, new Path(args[1]));
        
        job1.waitForCompletion(true);
     
        Job job2 = new Job(getConf(), "WordCount");
        job2.setJarByClass(WordCount.class);
        job2.setOutputKeyClass(Text.class);
        job2.setOutputValueClass(IntWritable.class);
        
        job2.setMapperClass(Map2.class);
        job2.setReducerClass(Reduce2.class);
        
        job2.setInputFormatClass(TextInputFormat.class);
        job2.setOutputFormatClass(TextOutputFormat.class);
        
        FileInputFormat.addInputPath(job2, new Path(args[1]));
        FileOutputFormat.setOutputPath(job2, new Path(args[2]));
        
        job2.waitForCompletion(true);
        
        return 0;
    }
    
    public static class Map1 extends Mapper<LongWritable, Text, Text, IntWritable> 
    {
        private final static IntWritable ONE = new IntWritable(1);
        private Text word = new Text();
        
        @Override
        public void map(LongWritable key, Text value, Context context)
        throws IOException, InterruptedException {
            for (String token: value.toString().split("\\s+")) 
            {
            	if(token.length()!=0)
                {           
                    for(int i=0;i<token.length();i++)
                    {
                        if(!Character.isLetter(token.charAt(i)))
                        {                               
                            token=token.substring(0,i)+token.substring(i+1);                        
                            i--;
                        }
                        token=token.toLowerCase();
                        
                    }
                    word.set(token);
                    context.write(word, ONE);    
            	}  
            }
        }
    }
    
    public static class Reduce1 extends Reducer<Text, IntWritable, Text, IntWritable> 
    {
        @Override
        public void reduce(Text key, Iterable<IntWritable> values, Context context) 
        throws IOException, InterruptedException 
        {
            int sum = 1;

            context.write(key, new IntWritable(sum));
        }
    }
    
    public static class Map2 extends Mapper<LongWritable, Text, Text, IntWritable> 
    {
        private final static IntWritable ONE = new IntWritable(1);
        private Text word = new Text();
        
        @Override
        public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException 
        {
            String [] token = value.toString().split("\\s+");
            
            word.set(Integer.toString(token[0].length()));
            context.write(word, ONE);
            
        }
    }
    
    public static class Reduce2 extends Reducer<Text, IntWritable, Text, IntWritable> 
    {
        @Override
        public void reduce(Text key, Iterable<IntWritable> values, Context context)
        throws IOException, InterruptedException 
        {
            int sum = 0;
            for (IntWritable val : values) 
            {
                sum += val.get();
            }
            context.write(key, new IntWritable(sum));
        }
    }
}


